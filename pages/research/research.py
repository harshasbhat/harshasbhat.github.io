#!/usr/bin/env python3
"""
research.py — generate the fault energy-budget radial diagram as SVG,
with an optional `highlight` set for staged talk visuals: pass a set of
segment ids and everything NOT in it gets dimmed (desaturated + faded),
independently on Ring A and Ring B — no parent/child linkage.

Usage:
    python3 research.py -o full.svg
    python3 research.py -o stage1.svg --highlight tidal,transient
"""

import argparse
import math
import random
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
                dim_opacity=0.28, dim_desat=0.6, dim_text_opacity=0.45, dim_arrows=True):
    """
    highlight: None -> no dimming, everyone drawn at full style (backward compatible).
               A set/list of segment ids -> any segment whose 'id' is NOT in it
               gets desaturated + faded (wedge, label, and — unless dim_arrows=False
               — its arrow too). Independent per call, so Ring A and Ring B are
               dimmed separately with their own highlight sets.
    """
    if arrow_span is None:
        arrow_span = (r1 + 8, r1 + 40)

    defs, wedges, labels, arrows = [], [], [], []
    for i in range(len(boundaries) - 1):
        a0, a1 = boundaries[i], boundaries[i + 1]
        seg = segments[i]
        seg_id = seg.get('id', seg['label'] if isinstance(seg['label'], str) else str(i))
        is_dim = (highlight is not None) and (seg_id not in highlight)

        base_color = seg['color']
        color = desaturate(base_color, dim_desat) if is_dim else base_color
        opacity = dim_opacity if is_dim else (0.25 if seg.get('empty') else seg.get('opacity', 0.7))
        text_opacity = dim_text_opacity if is_dim else 1.0

        dash = ' stroke-dasharray="4 3"' if seg.get('empty') else ''
        title = f"<title>{esc(seg.get('full', seg['label'] if isinstance(seg['label'], str) else seg_id))}</title>" if seg.get('full') else ''
        wedges.append(
            f'<path d="{donut_path(cx, cy, r0, r1, a0+2, a1-2)}" fill="{color}" '
            f'fill-opacity="{opacity}" stroke="#f0f2f0" stroke-width="1"{dash}>{title}</path>'
        )
        mid = (a0 + a1) / 2
        text_r = seg.get('text_r', (r0 + r1) / 2)
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

    return "\n".join(defs), "\n".join(wedges), "\n".join(labels), "\n".join(arrows)

# =============================================================== diagram ===

def build_diagram(width=800, height=980, highlight_A=None, highlight_B=None):
    """
    highlight_A / highlight_B: None (no dimming) or a set of ids to keep
    at full brightness on that ring specifically. Independent — no
    parent/child auto-linkage between rings.
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

    defsA, wA, lA, aA = build_ring(cx, cy, R_A0, R_A1, ringA_boundaries, ringA_segments,
                                    arrow_span=None, highlight=highlight_A)
    defsB, wB, lB, aB = build_ring(cx, cy, R_B0, R_B1, ringB_boundaries, ringB_segments,
                                    arrow_span=(1.05 * R_A1, 0.95 * R_B0), highlight=highlight_B)

    center = (
        f'<text x="{cx}" y="{cy-6}" font-family="Helvetica" font-weight="600" font-size="15" fill="#EDEAE2" text-anchor="middle">Observable</text>\n'
        f'<text x="{cx}" y="{cy+14}" font-family="Helvetica" font-weight="600" font-size="15" fill="#EDEAE2" text-anchor="middle">Energy Budget</text>'
    )

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
<defs>
{defsA}
{defsB}
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
    return svg

# =================================================================== CLI ===

ALL_IDS_A = {'radiated', 'dissipated', 'potential'}
ALL_IDS_B = {'source_ground', 'tsunami', 'friction', 'offfault_damage', 'longterm_viscous',
             'constant_rate', 'tidal', 'hydrological', 'transient', 'fault_interaction'}

ID_RING_MAP = {**{i: 'A' for i in ALL_IDS_A}, **{i: 'B' for i in ALL_IDS_B}}

def render_sequence(ids, prefix="stage", verify_render=True, **diagram_kwargs):
    """
    ids: flat list like ['potential', 'radiated', 'dissipated', 'offfault_damage', 'source_ground']
         Each id is looked up in ID_RING_MAP to decide Ring A vs Ring B automatically.
         Highlights accumulate — stage N includes everything from stages 1..N.
    Writes flat files: stage01_potential.svg, stage02_radiated.svg, ...
    Returns the list of file paths written.
    """
    hA, hB = set(), set()
    paths = []
    for i, seg_id in enumerate(ids, start=1):
        ring = ID_RING_MAP.get(seg_id)
        if ring is None:
            raise ValueError(f"Unknown id '{seg_id}' — not in Ring A {sorted(ALL_IDS_A)} "
                              f"or Ring B {sorted(ALL_IDS_B)}.")
        (hA if ring == 'A' else hB).add(seg_id)

        svg = build_diagram(highlight_A=set(hA), highlight_B=set(hB), **diagram_kwargs)
        path = f"{prefix}{i:02d}_{seg_id}.svg"
        with open(path, "w") as f:
            f.write(svg)
        paths.append(path)
    return paths

def render_gif(ids, gif_path="sequence.gif", frame_ms=900, hold_last_ms=2500,
                viewport=(900, 1100), scale=2, keep_svgs=True, keep_pngs=False,
                **diagram_kwargs):
    """
    Build a cumulative staged sequence (same semantics as render_sequence)
    and assemble it into an animated GIF.

    Requires playwright (for correct SVG rendering — textPath support in
    PIL/cairosvg is unreliable) and Pillow (for GIF assembly).

    frame_ms: duration of each non-final frame, in milliseconds.
    hold_last_ms: duration the final (fully-built) frame holds, in milliseconds
                  — usually longer, so the finished diagram doesn't flash by.
    scale: device_scale_factor for rendering — higher = crisper but bigger file.
    keep_svgs / keep_pngs: whether to leave the intermediate files on disk.
    Returns the gif_path written.
    """
    from playwright.sync_api import sync_playwright
    from PIL import Image
    import os

    svg_paths = render_sequence(ids, **diagram_kwargs)
    png_paths = [p.replace(".svg", ".png") for p in svg_paths]

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': viewport[0], 'height': viewport[1]},
                                 device_scale_factor=scale)
        for svg_p, png_p in zip(svg_paths, png_paths):
            page.goto(f"file://{os.path.abspath(svg_p)}")
            page.screenshot(path=png_p)
        browser.close()

    frames = [Image.open(p).convert("RGBA") for p in png_paths]
    # flatten onto white (GIF has no real alpha compositing across frames)
    flat_frames = []
    for f in frames:
        bg = Image.new("RGB", f.size, (255, 255, 255))
        bg.paste(f, mask=f.split()[3])
        flat_frames.append(bg)

    durations = [frame_ms] * (len(flat_frames) - 1) + [hold_last_ms]
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