#!/usr/bin/env python3
"""
energy_budget_svg.py — core library: generates the fault energy-budget
radial diagram as SVG. Handles geometry, curved labels, arrows, per-segment
images, and highlight/dim/grow staging.

This file also has its own minimal CLI (below) for the single-diagram case
only — full diagram or one highlighted snapshot, no sequences or GIFs:
    python3 energy_budget_svg.py -o full.svg
    python3 energy_budget_svg.py -o stage1.svg --highlight-a dissipated --highlight-b tidal,transient

For staged sequences and GIFs, use master.py instead — see README.md for
the full picture (all parameters, the image registry, growth/shrink
percentages, and which SVG->PNG renderers actually work on this diagram).
"""

import argparse
import math
import os
import re
from matplotlib.textpath import TextPath
from matplotlib.font_manager import FontProperties

# ============================================================== geometry ===

def pt(cx, cy, r, deg):
    rad = math.radians(deg)
    return cx + r * math.sin(rad), cy - r * math.cos(rad)

def donut_path(cx, cy, r0, r1, a0, a1):
    span = a1 - a0
    if span >= 359.999:
        mid = a0 + 180
        return donut_path(cx, cy, r0, r1, a0, mid) + " " + donut_path(cx, cy, r0, r1, mid, a1)
    large = 1 if span > 180 else 0
    ox0, oy0 = pt(cx, cy, r1, a0); ox1, oy1 = pt(cx, cy, r1, a1)
    ix1, iy1 = pt(cx, cy, r0, a1); ix0, iy0 = pt(cx, cy, r0, a0)
    return (f"M {ox0:.2f} {oy0:.2f} A {r1} {r1} 0 {large} 1 {ox1:.2f} {oy1:.2f} "
            f"L {ix1:.2f} {iy1:.2f} A {r0} {r0} 0 {large} 0 {ix0:.2f} {iy0:.2f} Z")

def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

# ------------------------------------------------------------- images ---

_image_data_uri_cache = {}

def image_to_data_uri(path):
    """Read an image file and return it as a base64 data URI, so the SVG
    stays self-contained (no external file references that break when the
    SVG is moved). Cached per path since the same image is often reused."""
    if path in _image_data_uri_cache:
        return _image_data_uri_cache[path]
    import base64
    import mimetypes
    mime, _ = mimetypes.guess_type(path)
    if mime is None:
        mime = "image/png"
    with open(path, "rb") as f:
        data = f.read()
    uri = f"data:{mime};base64,{base64.b64encode(data).decode('ascii')}"
    _image_data_uri_cache[path] = uri
    return uri

def circular_image(x, y, diameter, image_path, id_hint="img"):
    """Return (defs_snippet, image_snippet) for an image clipped to a circle,
    centered at (x, y)."""
    _id_counter[0] += 1
    clip_id = f"{id_hint}{_id_counter[0]}"
    uri = image_to_data_uri(image_path)
    r = diameter / 2
    defs = f'<clipPath id="{clip_id}"><circle cx="0" cy="0" r="{r}"/></clipPath>'
    img = (f'<image href="{uri}" x="{-r}" y="{-r}" width="{diameter}" height="{diameter}" '
           f'preserveAspectRatio="xMidYMid slice" clip-path="url(#{clip_id})" '
           f'transform="translate({x:.2f} {y:.2f})"/>')
    return defs, img

# --------------------------------------------------------- svg -> png ---
# Single canonical implementation, used by render_gif() below AND by
# master.py / svg_to_png.py. If you're seeing ModuleNotFoundError: playwright
# from somewhere that ISN'T this function, that call site has its own copy
# that's drifted out of sync with this one — route it through here instead.

def _svg_to_png_api(svg_path, png_path, viewport, scale):
    """Playwright Python API — supports device_scale_factor."""
    import os
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(
            viewport={"width": viewport[0], "height": viewport[1]},
            device_scale_factor=scale,
        )
        page.goto(f"file://{os.path.abspath(svg_path)}")
        page.screenshot(path=png_path)
        browser.close()

def _svg_to_png_cli(svg_path, png_path, viewport):
    """Fallback: shell out to the `playwright` CLI command. Works even when
    Playwright was installed via `pipx` (which isolates it from the system
    Python, so `import playwright` fails there even though the CLI works).
    No device_scale_factor support via this path — always renders at 1x."""
    import os
    import subprocess
    subprocess.run(
        ["playwright", "screenshot", f"--viewport-size={viewport[0]},{viewport[1]}",
         f"file://{os.path.abspath(svg_path)}", png_path],
        check=True, capture_output=True, text=True,
    )

def svg_to_png(svg_path, png_path, viewport=(900, 1100), scale=2):
    """Convert one SVG to PNG. Tries the Playwright Python API first (supports
    scale); if playwright isn't importable (e.g. a pipx install), falls back
    to the playwright CLI automatically (fixed at 1x, no scale support)."""
    try:
        _svg_to_png_api(svg_path, png_path, viewport, scale)
    except ImportError:
        import sys
        print(f"  (playwright not importable as a Python module — falling back "
              f"to the CLI, no {scale}x scaling)", file=sys.stderr)
        _svg_to_png_cli(svg_path, png_path, viewport)

# --------------------------------------------------------- output dirs ---
# PowerPoint (and some other tools) scramble/mangle pasted SVGs — dropped
# text, broken curves, wrong colors. PNG is the safe format for slides. So
# every SVG this library writes gets sorted into svg/, and a matching PNG
# (the thing you'd actually paste into a deck) goes into png/ automatically,
# with GIFs in their own gif/ — three clearly separated folders instead of
# everything flat in one directory.

def ensure_output_dirs(base_dir="."):
    """Create (if needed) and return (svg_dir, png_dir, gif_dir) under base_dir."""
    svg_dir = os.path.join(base_dir, "svg")
    png_dir = os.path.join(base_dir, "png")
    gif_dir = os.path.join(base_dir, "gif")
    for d in (svg_dir, png_dir, gif_dir):
        os.makedirs(d, exist_ok=True)
    return svg_dir, png_dir, gif_dir

def save_diagram(svg_content, name, base_dir=".", also_png=True, scale=2, viewport=None):
    """
    Write one build_diagram() SVG to base_dir/svg/<name>.svg, and — by
    default — also render a matching PNG to base_dir/png/<name>.png.
    viewport: (w, h) for the PNG render. None = read it off the SVG's own
    width/height attributes (the auto-cropped size), which is almost always
    what you want.
    Returns (svg_path, png_path) — png_path is None if also_png=False.
    """
    svg_dir, png_dir, _ = ensure_output_dirs(base_dir)
    svg_path = os.path.join(svg_dir, f"{name}.svg")
    with open(svg_path, "w") as f:
        f.write(svg_content)

    png_path = None
    if also_png:
        if viewport is None:
            w = int(re.search(r'width="(\d+)"', svg_content).group(1))
            h = int(re.search(r'height="(\d+)"', svg_content).group(1))
            viewport = (w, h)
        png_path = os.path.join(png_dir, f"{name}.png")
        svg_to_png(svg_path, png_path, viewport=viewport, scale=scale)

    return svg_path, png_path

# --- Registered images: edit paths here. Registering an image does NOT show
# it — that's controlled per-call via build_diagram(show_images=..., 
# show_center_image=...), so you can flip images on/off without touching
# this registry. Any id not in SEGMENT_IMAGES is simply never shown, even
# if requested. ---
SEGMENT_IMAGES = {
    # 'friction': '/path/to/someone.jpg',
    # 'tidal': '/path/to/something-else.jpg',
}
CENTER_IMAGE = None  # e.g. '/path/to/center-photo.jpg'

# ------------------------------------------------------- dim/desaturate ---

def desaturate(hex_color, factor=0.55, gray="#9AA0A6"):
    """Blend hex_color toward `gray` by `factor` (0=original, 1=full gray)."""
    hex_color = hex_color.lstrip('#')
    gray = gray.lstrip('#')
    r1, g1, b1 = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    r2, g2, b2 = int(gray[0:2], 16), int(gray[2:4], 16), int(gray[4:6], 16)
    r = round(r1 + (r2 - r1) * factor)
    g = round(g1 + (g2 - g1) * factor)
    b = round(b1 + (b2 - b1) * factor)
    return f"#{r:02X}{g:02X}{b:02X}"

# ========================================================= curved labels ===

_id_counter = [0]
_prop_cache = {}

def _prop(weight="bold"):
    if weight not in _prop_cache:
        _prop_cache[weight] = FontProperties(family="Helvetica", weight=weight)
    return _prop_cache[weight]

def _text_width(text, font_size):
    tp = TextPath((0, 0), text, size=font_size, prop=_prop("bold"))
    return tp.get_extents().width

_BASELINE = {'top': 'hanging', 'mid': 'middle', 'bottom': 'alphabetic'}

def _curved_line(cx, cy, r, angle_deg, text, font_size, font_family,
                  weight, fill, vpos, pad_ratio, flip, opacity=1.0):
    _id_counter[0] += 1
    pid = f"curvelbl{_id_counter[0]}"
    width = _text_width(text, font_size)
    span_deg = math.degrees((width * pad_ratio) / r)
    mid = angle_deg % 360
    reverse = (90 < mid <= 270) if flip is None else flip
    a0, a1 = angle_deg - span_deg / 2, angle_deg + span_deg / 2
    start, end, sweep = (a1, a0, 0) if reverse else (a0, a1, 1)
    large = 1 if abs(a1 - a0) > 180 else 0
    x0, y0 = pt(cx, cy, r, start)
    x1, y1 = pt(cx, cy, r, end)
    path_d = f"M {x0:.2f} {y0:.2f} A {r} {r} 0 {large} {sweep} {x1:.2f} {y1:.2f}"
    baseline = _BASELINE.get(vpos, 'alphabetic')
    defs = f'<path id="{pid}" d="{path_d}" fill="none"/>'
    label = (f'<text font-family="{font_family}" font-weight="{weight}" font-size="{font_size}" '
             f'fill="{fill}" fill-opacity="{opacity}" dominant-baseline="{baseline}">'
             f'<textPath href="#{pid}" startOffset="50%" text-anchor="middle">{esc(text)}</textPath>'
             f'</text>')
    return defs, label

def curved_label(cx, cy, r, angle_deg, text, font_size=14, font_family="Helvetica",
                  weight="600", fill="#EDEAE2", vpos="mid", pad_ratio=1.25, flip=None,
                  line_height=None, opacity=1.0):
    lines = list(text) if isinstance(text, (list, tuple)) else [text]
    n = len(lines)
    lh = line_height if line_height is not None else font_size * 1.3
    mid = angle_deg % 360
    reverse = (90 < mid <= 270) if flip is None else flip
    if reverse and n > 1:
        lines = lines[::-1]
    defs_all, label_all = [], []
    for i, line in enumerate(lines):
        offset = ((n - 1) / 2 - i) * lh
        d, l = _curved_line(cx, cy, r + offset, angle_deg, line, font_size,
                             font_family, weight, fill, vpos, pad_ratio, flip, opacity)
        defs_all.append(d)
        label_all.append(l)
    return "\n".join(defs_all), "\n".join(label_all)

# ============================================================ arrows =======

_arrow_marker_ids = {}

def _arrow_marker_defs(color, size=8):
    key = color
    if key in _arrow_marker_ids:
        return _arrow_marker_ids[key], ""
    mid = f"arrowhead{len(_arrow_marker_ids)}"
    _arrow_marker_ids[key] = mid
    defs = (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" '
            f'markerWidth="{size}" markerHeight="{size}" orient="auto">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{color}"/></marker>')
    return mid, defs

def radial_arrow(cx, cy, angle_deg, r_in, r_out, direction, color,
                  stroke_width=2, head_size=8, opacity=1.0):
    if direction not in ('in', 'out', 'both'):
        return "", ""
    mid_id, marker_defs = _arrow_marker_defs(color, size=head_size)
    x_in, y_in = pt(cx, cy, r_in, angle_deg)
    x_out, y_out = pt(cx, cy, r_out, angle_deg)
    op = f' stroke-opacity="{opacity}"'
    lines = []
    if direction == 'out':
        lines.append(f'<line x1="{x_in:.2f}" y1="{y_in:.2f}" x2="{x_out:.2f}" y2="{y_out:.2f}" '
                      f'stroke="{color}"{op} stroke-width="{stroke_width}" marker-end="url(#{mid_id})"/>')
    elif direction == 'in':
        lines.append(f'<line x1="{x_out:.2f}" y1="{y_out:.2f}" x2="{x_in:.2f}" y2="{y_in:.2f}" '
                      f'stroke="{color}"{op} stroke-width="{stroke_width}" marker-end="url(#{mid_id})"/>')
    elif direction == 'both':
        r_mid = (r_in + r_out) / 2
        x_mid, y_mid = pt(cx, cy, r_mid, angle_deg)
        lines.append(f'<line x1="{x_mid:.2f}" y1="{y_mid:.2f}" x2="{x_out:.2f}" y2="{y_out:.2f}" '
                      f'stroke="{color}"{op} stroke-width="{stroke_width}" marker-end="url(#{mid_id})"/>')
        lines.append(f'<line x1="{x_mid:.2f}" y1="{y_mid:.2f}" x2="{x_in:.2f}" y2="{y_in:.2f}" '
                      f'stroke="{color}"{op} stroke-width="{stroke_width}" marker-end="url(#{mid_id})"/>')
    return marker_defs, "\n".join(lines)

# =============================================================== rings =====

def build_ring(cx, cy, r0, r1, boundaries, segments, arrow_span=None, highlight=None,
                dim_opacity=0.28, dim_desat=0.6, dim_text_opacity=0.45, dim_arrows=True,
                highlight_grow_pct=0, dim_shrink_pct=0):
    """
    highlight: None -> no dimming, everyone drawn at full style (backward compatible).
               A set/list of segment ids -> any segment whose 'id' is NOT in it
               gets desaturated + faded (wedge, label, and — unless dim_arrows=False
               — its arrow too). Independent per call, so Ring A and Ring B are
               dimmed separately with their own highlight sets.
    highlight_grow_pct: fraction of ring thickness (r1-r0) a HIGHLIGHTED wedge's
                         outer radius extends by. E.g. 0.25 = pops out 25% of the
                         ring's thickness past the normal edge.
    dim_shrink_pct: fraction of ring thickness a DIMMED wedge's outer radius
                     pulls inward by. E.g. 0.15 = shrinks 15%.
    Both only apply when highlight is not None; r0 (inner boundary) never moves
    for anyone, so the ring's inner edge stays a clean, stable circle.
    Returns (defs_svg, wedges_svg, labels_svg, arrows_svg, grow_px, max_extent) —
    grow_px is how many pixels highlighted wedges extended by (for arrow-span
    handoff to an outer ring); max_extent is the furthest radius ANY drawn
    element (wedge, arrow, or image) actually reached from (cx, cy) this call —
    used to auto-crop the final SVG's viewBox tightly instead of a fixed canvas.
    """
    thickness = r1 - r0
    grow_px = highlight_grow_pct * thickness if highlight is not None else 0
    shrink_px = dim_shrink_pct * thickness
    max_extent = r1  # never smaller than the ring's own nominal outer edge

    if arrow_span is None:
        arrow_span = (r1 + 8, r1 + 40)

    defs, wedges, labels, arrows = [], [], [], []
    for i in range(len(boundaries) - 1):
        a0, a1 = boundaries[i], boundaries[i + 1]
        seg = segments[i]
        seg_id = seg.get('id', seg['label'] if isinstance(seg['label'], str) else str(i))
        is_dim = (highlight is not None) and (seg_id not in highlight)
        is_grown = (highlight is not None) and (not is_dim) and highlight_grow_pct

        base_color = seg['color']
        color = desaturate(base_color, dim_desat) if is_dim else base_color
        opacity = dim_opacity if is_dim else (0.25 if seg.get('empty') else seg.get('opacity', 0.7))
        text_opacity = dim_text_opacity if is_dim else 1.0

        if is_grown:
            r1_wedge = r1 + grow_px
        elif is_dim and dim_shrink_pct:
            r1_wedge = r1 - shrink_px
        else:
            r1_wedge = r1
        max_extent = max(max_extent, r1_wedge)

        dash = ' stroke-dasharray="4 3"' if seg.get('empty') else ''
        title = f"<title>{esc(seg.get('full', seg['label'] if isinstance(seg['label'], str) else seg_id))}</title>" if seg.get('full') else ''
        wedges.append(
            f'<path d="{donut_path(cx, cy, r0, r1_wedge, a0+2, a1-2)}" fill="{color}" '
            f'fill-opacity="{opacity}" stroke="#f0f2f0" stroke-width="1"{dash}>{title}</path>'
        )
        mid = (a0 + a1) / 2
        text_r = seg.get('text_r', (r0 + r1) / 2)
        if is_grown:
            text_r += grow_px / 2
        elif is_dim and dim_shrink_pct:
            text_r -= shrink_px / 2
        text_fill = desaturate(seg.get('text_fill', '#EDEAE2'), dim_desat) if is_dim else seg.get('text_fill', '#EDEAE2')
        d, l = curved_label(
            cx, cy, text_r, mid, seg['label'],
            font_size=seg.get('font_size', 12),
            fill=text_fill,
            vpos=seg.get('vpos', 'mid'),
            flip=seg.get('flip', None),
            line_height=seg.get('line_height', None),
            opacity=text_opacity,
        )
        defs.append(d)
        labels.append(l)

        arrow_dir = seg.get('arrow')
        if arrow_dir and not (is_dim and dim_arrows):
            ar_in = seg.get('arrow_r_in', arrow_span[0])
            ar_out = seg.get('arrow_r_out', arrow_span[1])
            ar_color = desaturate(seg.get('arrow_color', seg['color']), dim_desat) if is_dim else seg.get('arrow_color', seg['color'])
            ad, al = radial_arrow(cx, cy, mid, ar_in, ar_out, arrow_dir, ar_color,
                                   stroke_width=seg.get('arrow_width', 2),
                                   head_size=seg.get('arrow_head_size', 8),
                                   opacity=(dim_text_opacity if is_dim else 1.0))
            if ad:
                defs.append(ad)
            if al:
                arrows.append(al)
            max_extent = max(max_extent, ar_in, ar_out)

        image_path = seg.get('image')
        if image_path:
            img_size = seg.get('image_size', 40)
            img_r = seg.get('image_r', r1_wedge + img_size / 2 + 12)  # r1_wedge accounts for this segment's own grow/shrink
            ix, iy = pt(cx, cy, img_r, mid)
            idf, img = circular_image(ix, iy, img_size, image_path, id_hint="segimg")
            defs.append(idf)
            arrows.append(img)  # drawn in the same pass as arrows: outside the wedge, on top
            max_extent = max(max_extent, img_r + img_size / 2)

    return "\n".join(defs), "\n".join(wedges), "\n".join(labels), "\n".join(arrows), grow_px, max_extent

# =============================================================== diagram ===

def build_diagram(width=800, height=980, highlight_A=None, highlight_B=None,
                   center_image=None, show_center_image=False, show_images=None,
                   show_center=True, center_text=None,
                   highlight_grow_pct=0.25, dim_shrink_pct=0.15,
                   force_viewbox=None, return_bounds=False,
                   background_color=None):
    """
    highlight_A / highlight_B: None (no dimming) or a set of ids to keep
    at full brightness on that ring specifically. Independent — no
    parent/child auto-linkage between rings.
    show_center: master on/off switch for the innermost circle's content.
    False = nothing drawn there at all (no text, no image) — a blank hub.
    True (default) = show text or an image, per the params below.
    center_text: a string, or a list of strings for multiple lines, e.g.
    ['My Diagram'] or ['Line One', 'Line Two']. If given, ALWAYS wins —
    shows this text regardless of center_image/show_center_image/CENTER_IMAGE,
    so this is the way to force text even when an image is registered.
    Omit it (leave as None) to get the default "Observable / Energy Budget"
    text, or an image if one's requested per the params below.
    center_image: explicit path override — if given (and center_text is
    NOT given), used regardless of show_center_image/CENTER_IMAGE. Replaces
    the center text entirely.
    show_center_image: if True (and center_image/center_text not explicitly
    given), uses CENTER_IMAGE from the registry above.
    show_images: set of Ring B segment ids to show their registered image
    for (looked up in SEGMENT_IMAGES), e.g. {'friction', 'tidal'}. Per-segment
    control, independent of highlight_B — an id can be highlighted without
    showing its image, or shown without being highlighted. None/empty = no
    images, regardless of what's registered.
    highlight_grow_pct: how far a HIGHLIGHTED wedge's outer edge extends,
    as a fraction of its ring's thickness (default 0.25 = 25%). Applies to
    both rings equally.
    dim_shrink_pct: how far a DIMMED wedge's outer edge pulls in, as a
    fraction of ring thickness (default 0.15 = 15%). Applies to both rings.
    force_viewbox: (vb_x, vb_y, vb_size) tuple — if given, skips the normal
    auto-crop computation and uses this fixed square viewBox instead. This
    is how a sequence keeps every stage the SAME size (see render_sequence),
    since auto-cropping each stage to ITS OWN content would make frames
    different sizes and the diagram would visibly jump around in a GIF.
    return_bounds: if True, returns (svg_string, (vb_x, vb_y, vb_size))
    instead of just svg_string — lets a caller find out how big a given
    configuration needs to be without necessarily using that render directly.
    background_color: None (default) = transparent, no background element at
    all. Any CSS color string (e.g. '#FFFFFF', 'white') = an opaque rect
    covering exactly the computed crop, drawn first so nothing sits behind it.
    """
    _arrow_marker_ids.clear()  # each SVG is self-contained; don't carry marker cache across calls
    cx, cy = width / 2, height * 0.55
    POT, RAD, DIS = "#177612", "#5FB7C7", "#B83511"
    R_A0, R_A1 = 100, 160
    R_B0, R_B1 = 210, 270
    rAfont = 17
    rBfont = rAfont * 0.85

    ringA_boundaries = [0, 90, 180, 360]
    ringA_segments = [
        {'id': 'radiated', 'label': 'Radiated', 'color': RAD, 'opacity': 0.82,
         'text_fill': '#0E1013', 'font_size': rAfont, 'vpos': 'mid'},
        {'id': 'dissipated', 'label': 'Dissipated', 'color': DIS, 'opacity': 0.82,
         'text_fill': '#0E1013', 'font_size': rAfont, 'vpos': 'mid'},
        {'id': 'potential', 'label': 'Potential', 'color': POT, 'opacity': 0.82,
         'text_fill': '#0E1013', 'font_size': rAfont, 'vpos': 'mid',
         'text_r': (R_A0 + R_A1) / 2, 'flip': False},
    ]

    ringB_boundaries = [0, 45, 90, 120, 150, 180, 216, 252, 288, 324, 360]
    ringB_segments = [
        {'id': 'source_ground', 'label': ['Source &', 'Ground Motion'],
         'full': 'Source & Ground Motion — radiation, attenuation', 'color': RAD, 'arrow': 'out'},
        {'id': 'tsunami', 'label': ['Tsunami &', 'Far-Field Coupling'],
         'full': 'Tsunami & Far-Field Coupling — radiated → ocean', 'color': RAD, 'arrow': 'out'},
        {'id': 'friction', 'label': ['Friction'], 'full': 'intensive properties', 'color': DIS, 'arrow': 'out'},
        {'id': 'offfault_damage', 'label': ['Off-Fault', 'Damage'], 'full': 'geometry of dissipation',
         'color': DIS, 'arrow': 'out'},
        {'id': 'longterm_viscous', 'label': ['Long-Term /', 'Viscous Flow'], 'full': 'geodynamic',
         'color': DIS, 'arrow': 'out'},
        {'id': 'constant_rate', 'label': ['Constant Stress', '/ Plate Rate'], 'full': 'steady, assumed',
         'color': POT, 'empty': False, 'arrow': 'in'},
        {'id': 'tidal', 'label': 'Tidal', 'full': 'Tidal loading', 'color': POT, 'arrow': 'in'},
        {'id': 'hydrological', 'label': 'Hydrological', 'full': 'Hydrological loading', 'color': POT, 'arrow': 'in'},
        {'id': 'transient', 'label': 'Transient', 'full': 'stress transfer, injection', 'color': POT, 'arrow': 'in'},
        {'id': 'fault_interaction', 'label': ['Fault', 'Interaction'], 'full': 'stress redistribution',
         'color': POT, 'arrow': 'in'},
    ]
    for s in ringB_segments:
        s.setdefault('font_size', rBfont)
        s.setdefault('opacity', 0.65)
        s.setdefault('vpos', 'mid')
        s.setdefault('text_r', (R_B0 + R_B1) / 2)
        if show_images and s['id'] in show_images and s['id'] in SEGMENT_IMAGES:
            s['image'] = SEGMENT_IMAGES[s['id']]
            s.setdefault('image_size', 44)

    if center_image is None and show_center_image:
        center_image = CENTER_IMAGE

    defsA, wA, lA, aA, growA_px, maxA = build_ring(cx, cy, R_A0, R_A1, ringA_boundaries, ringA_segments,
                                                    arrow_span=None, highlight=highlight_A,
                                                    highlight_grow_pct=highlight_grow_pct, dim_shrink_pct=dim_shrink_pct)
    # Ring B's arrow start is derived from however far Ring A actually grew this call,
    # plus a small fixed gap — self-adjusting, so it can never collide regardless of
    # what highlight_grow_pct is set to.
    arrow_gap = 6
    defsB, wB, lB, aB, growB_px, maxB = build_ring(cx, cy, R_B0, R_B1, ringB_boundaries, ringB_segments,
                                                    arrow_span=(R_A1 + growA_px + arrow_gap, 0.95 * R_B0),
                                                    highlight=highlight_B,
                                                    highlight_grow_pct=highlight_grow_pct, dim_shrink_pct=dim_shrink_pct)

    center_defs = ""
    if not show_center:
        center = ""
    elif center_text is not None:
        lines = list(center_text) if isinstance(center_text, (list, tuple)) else [center_text]
        line_height = 20
        center = "\n".join(
            f'<text x="{cx}" y="{cy + (i - (len(lines)-1)/2)*line_height + 5}" '
            f'font-family="Helvetica" font-weight="600" font-size="15" fill="#EDEAE2" '
            f'text-anchor="middle">{esc(line)}</text>'
            for i, line in enumerate(lines)
        )
    elif center_image:
        img_diameter = 2 * (R_A0 - 12)  # small padding inside Ring A's inner edge
        cdef, cimg = circular_image(cx, cy, img_diameter, center_image, id_hint="centerimg")
        center_defs = cdef
        center = cimg
    else:
        center = (
            f'<text x="{cx}" y="{cy-6}" font-family="Helvetica" font-weight="600" font-size="15" fill="#EDEAE2" text-anchor="middle">Observable</text>\n'
            f'<text x="{cx}" y="{cy+14}" font-family="Helvetica" font-weight="600" font-size="15" fill="#EDEAE2" text-anchor="middle">Energy Budget</text>'
        )

    # Tight crop: the diagram is radially symmetric around (cx, cy), so the
    # true content bounds are a circle of radius = furthest thing drawn
    # (wedge, arrow, or image) on either ring, plus a little padding —
    # computed from what actually got drawn this call, not a fixed canvas.
    # UNLESS force_viewbox is given (used by render_sequence to keep every
    # stage in a GIF the same size — see docstring above).
    if force_viewbox is not None:
        vb_x, vb_y, vb_size = force_viewbox
    else:
        content_r = max(maxA, maxB, R_A0)  # never smaller than the hub itself
        pad = 24
        vb = content_r + pad
        vb_x, vb_y = cx - vb, cy - vb
        vb_size = 2 * vb

    bg_rect = (
        f'<rect x="{vb_x:.1f}" y="{vb_y:.1f}" width="{vb_size:.1f}" height="{vb_size:.1f}" fill="{background_color}"/>'
        if background_color else ""
    )

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb_x:.1f} {vb_y:.1f} {vb_size:.1f} {vb_size:.1f}" width="{vb_size:.0f}" height="{vb_size:.0f}">
{bg_rect}
<defs>
{defsA}
{defsB}
{center_defs}
</defs>
{wA}
{wB}
{aA}
{aB}
{lA}
{lB}
{center}
</svg>
'''
    if return_bounds:
        return svg, (vb_x, vb_y, vb_size)
    return svg

# =================================================================== CLI ===

ALL_IDS_A = {'radiated', 'dissipated', 'potential'}
ALL_IDS_B = {'source_ground', 'tsunami', 'friction', 'offfault_damage', 'longterm_viscous',
             'constant_rate', 'tidal', 'hydrological', 'transient', 'fault_interaction'}

ID_RING_MAP = {**{i: 'A' for i in ALL_IDS_A}, **{i: 'B' for i in ALL_IDS_B}}

def render_sequence(ids, prefix="stage", verify_render=True,
                     images_follow_sequence=False,
                     show_images_from=None, show_center_image_from=None,
                     base_dir=".", also_png=True, png_scale=2,
                     **diagram_kwargs):
    """
    ids: flat list like ['potential', 'radiated', 'dissipated', 'offfault_damage', 'source_ground']
         Each id is looked up in ID_RING_MAP to decide Ring A vs Ring B automatically.
         Highlights accumulate — stage N includes everything from stages 1..N.

    images_follow_sequence: the simple case — one flag, no per-id timing to
        specify. If True, a Ring B id's image (from SEGMENT_IMAGES) appears
        starting exactly at the stage where that id itself first appears in
        `ids`, and stays visible every stage after — same moment its wedge
        gets highlighted, no separate configuration needed. An id with no
        registered image just never shows one. If False (default), images
        are controlled the old way, via show_images_from or a static
        show_images in diagram_kwargs.

    show_images_from: optional dict {segment_id: stage_number}, stage_number
        1-indexed matching position in `ids`, for when you want an image to
        appear at a DIFFERENT stage than the one where its own id is reached
        (e.g. reveal an image ahead of or behind its wedge's own highlight).
        Ignored if images_follow_sequence=True.

    show_center_image_from: optional int (1-indexed stage) — CENTER_IMAGE
        appears starting at that stage onward. None = never shown via this
        mechanism (a static show_center_image=True in diagram_kwargs still
        works independently, showing it every stage).

    base_dir: SVGs go in base_dir/svg/, PNGs (if also_png) in base_dir/png/ —
        both created automatically if they don't exist.
    prefix: filenames are f"{prefix}{stage_number:02d}_{id}". If you call
        render_sequence/render_gif MORE THAN ONCE into the same base_dir,
        give each call a DIFFERENT prefix — otherwise the second call's
        files silently overwrite the first's (same filenames, same folder).
    also_png: also render a matching PNG per stage (default True) — PNG is
        the safe format for pasting into PowerPoint, which is known to
        scramble/mangle SVGs.
    png_scale: device scale factor for the PNG renders.

    Returns (svg_paths, png_paths) — png_paths is [] if also_png=False.

    Canvas: every stage shares ONE fixed viewBox, sized for the LAST (fullest)
    stage's content — computed once up front — rather than each stage
    auto-cropping to its own content. Otherwise frames would be different
    sizes and the diagram would visibly jump around when played as a GIF.
    """
    svg_dir, png_dir, _ = ensure_output_dirs(base_dir)

    # First pass: figure out the final cumulative state (everything highlighted,
    # every image eventually shown) purely to compute the shared canvas size.
    final_hA, final_hB = set(), set()
    for seg_id in ids:
        ring = ID_RING_MAP.get(seg_id)
        if ring is None:
            raise ValueError(f"Unknown id '{seg_id}' — not in Ring A {sorted(ALL_IDS_A)} "
                              f"or Ring B {sorted(ALL_IDS_B)}.")
        (final_hA if ring == 'A' else final_hB).add(seg_id)

    final_kwargs = dict(diagram_kwargs)
    if images_follow_sequence:
        final_kwargs['show_images'] = {sid for sid in final_hB if sid in SEGMENT_IMAGES}
    elif show_images_from:
        final_kwargs['show_images'] = set(show_images_from.keys())
    if show_center_image_from is not None:
        final_kwargs['show_center_image'] = True
    _, shared_bounds = build_diagram(highlight_A=final_hA, highlight_B=final_hB,
                                      return_bounds=True, **final_kwargs)
    viewport = (int(shared_bounds[2]), int(shared_bounds[2]))  # square, side = vb_size

    hA, hB = set(), set()
    svg_paths, png_paths = [], []
    for i, seg_id in enumerate(ids, start=1):
        ring = ID_RING_MAP.get(seg_id)
        (hA if ring == 'A' else hB).add(seg_id)

        stage_kwargs = dict(diagram_kwargs)
        if images_follow_sequence:
            stage_kwargs['show_images'] = {sid for sid in hB if sid in SEGMENT_IMAGES}
        elif show_images_from:
            stage_kwargs['show_images'] = {sid for sid, from_stage in show_images_from.items()
                                            if i >= from_stage}
        if show_center_image_from is not None:
            stage_kwargs['show_center_image'] = i >= show_center_image_from

        svg = build_diagram(highlight_A=set(hA), highlight_B=set(hB),
                             force_viewbox=shared_bounds, **stage_kwargs)
        name = f"{prefix}{i:02d}_{seg_id}"
        svg_path = os.path.join(svg_dir, f"{name}.svg")
        with open(svg_path, "w") as f:
            f.write(svg)
        svg_paths.append(svg_path)

        if also_png:
            png_path = os.path.join(png_dir, f"{name}.png")
            svg_to_png(svg_path, png_path, viewport=viewport, scale=png_scale)
            png_paths.append(png_path)

    return svg_paths, png_paths

def render_gif(ids, gif_name="sequence", frame_ms=900, hold_last_ms=2500,
                scale=2, base_dir=".", keep_svgs=True, keep_pngs=True,
                **diagram_kwargs):
    """
    Build a cumulative staged sequence (same semantics as render_sequence)
    and assemble it into an animated GIF.

    Requires playwright (for correct SVG rendering — textPath support in
    PIL/cairosvg is unreliable) and Pillow (for GIF assembly).

    frame_ms: duration of each non-final frame, in milliseconds.
    hold_last_ms: duration the final (fully-built) frame holds, in milliseconds
                  — usually longer, so the finished diagram doesn't flash by.
    scale: device_scale_factor for the PNG renders — higher = crisper but bigger file.
    base_dir: SVGs in base_dir/svg/, PNGs in base_dir/png/, the GIF itself in
        base_dir/gif/ — all created automatically. Reuses render_sequence's
        own PNG rendering rather than rendering each frame twice.
    keep_svgs / keep_pngs: whether to leave the per-stage SVG/PNG files on
        disk after the GIF is assembled (default True for both now — PNG in
        particular is worth keeping as its own deliverable, since it's the
        safe format for pasting into PowerPoint, which is known to
        scramble/mangle SVGs).
    Returns the gif_path written (inside base_dir/gif/).
    """
    from PIL import Image

    svg_paths, png_paths = render_sequence(
        ids, base_dir=base_dir, also_png=True, png_scale=scale, **diagram_kwargs
    )

    frames = [Image.open(p).convert("RGBA") for p in png_paths]
    # flatten onto white (GIF has no real alpha compositing across frames)
    flat_frames = []
    for f in frames:
        bg = Image.new("RGB", f.size, (255, 255, 255))
        bg.paste(f, mask=f.split()[3])
        flat_frames.append(bg)

    durations = [frame_ms] * (len(flat_frames) - 1) + [hold_last_ms]
    _, _, gif_dir = ensure_output_dirs(base_dir)
    gif_path = os.path.join(gif_dir, f"{gif_name}.gif")
    flat_frames[0].save(
        gif_path, save_all=True, append_images=flat_frames[1:],
        duration=durations, loop=0, optimize=False,
    )

    if not keep_pngs:
        for p in png_paths:
            os.remove(p)
    if not keep_svgs:
        for p in svg_paths:
            os.remove(p)

    return gif_path


def main():
    parser = argparse.ArgumentParser(description="Generate the fault energy-budget radial SVG.")
    parser.add_argument("-o", "--output", default="energy-budget-radial.svg")
    parser.add_argument("--width", type=int, default=800)
    parser.add_argument("--height", type=int, default=980)
    parser.add_argument("--highlight-a", default=None, help="comma-separated ids to keep bright on Ring A")
    parser.add_argument("--highlight-b", default=None, help="comma-separated ids to keep bright on Ring B")
    args = parser.parse_args()

    hA = set(args.highlight_a.split(',')) if args.highlight_a else None
    hB = set(args.highlight_b.split(',')) if args.highlight_b else None

    svg = build_diagram(width=args.width, height=args.height, highlight_A=hA, highlight_B=hB)
    with open(args.output, "w") as f:
        f.write(svg)

    n_labels = svg.count("<textPath")
    print(f"Wrote {args.output} ({len(svg):,} bytes, {n_labels} curved labels).")

if __name__ == "__main__":
    main()
