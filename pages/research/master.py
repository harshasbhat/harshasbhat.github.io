#!/usr/bin/env python3
"""
master.py — one entry point for the energy-budget diagram.

Two modes:
  full      generate the complete diagram, no dimming -> one SVG
  sequence  generate a cumulative staged highlight sequence -> individual
            SVGs (kept) + one assembled GIF

Usage:
    python3 master.py full -o diagram.svg
    python3 master.py sequence potential radiated dissipated offfault_damage source_ground -o sequence.gif

Requires energy_budget_svg.py in the same directory (or on PYTHONPATH),
and Pillow (`pip3 install pillow` or `pipx install pillow` etc.) for the
GIF assembly step. For rendering SVG->PNG, this script will use the
Playwright Python API if it's importable, and fall back automatically to
shelling out to the `playwright` CLI command if not (e.g. if Playwright
was installed via `pipx`, which isolates it from the system Python and
makes `import playwright` fail even though the CLI command works fine).

# --- Valid ids for `python3 master.py sequence ...` and render_sequence() ---
#
# Ring A (the three balance terms):
#   'radiated'          Radiated Energy (E_R)
#   'dissipated'        Observable Dissipation (D_O)
#   'potential'         Observable Potential Energy
#
# Ring B (the ten sub-channels):
#   source_ground       Source & Ground Motion       [Radiated]
#   tsunami             Tsunami & Far-Field Coupling  [Radiated]
#   friction            Friction                     [Dissipated]
#   offfault_damage     Off-Fault Damage              [Dissipated]
#   longterm_viscous    Long-Term / Viscous Flow      [Dissipated]
#   constant_rate       Constant Stress / Plate Rate  [Potential, drawn dashed/empty]
#   tidal               Tidal                         [Potential]
#   hydrological        Hydrological                  [Potential]
#   transient           Transient                     [Potential]
#   fault_interaction   Fault Interaction             [Potential]
#
# Any id not in one of these two lists will raise ValueError from render_sequence().

"""

import argparse
import os
import subprocess
import sys

import research as ebs

# ------------------------------------------------------- SVG -> PNG ---

def _svg_to_png_api(svg_path, png_path, viewport, scale):
    """Try the Playwright Python API (supports device_scale_factor)."""
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
    """Fallback: shell out to the `playwright` CLI (works with pipx installs).
    Note: the CLI has no --device-scale-factor flag, so this path is always 1x."""
    subprocess.run(
        ["playwright", "screenshot", f"--viewport-size={viewport[0]},{viewport[1]}",
         f"file://{os.path.abspath(svg_path)}", png_path],
        check=True, capture_output=True, text=True,
    )

def svg_to_png(svg_path, png_path, viewport=(900, 1100), scale=2):
    try:
        _svg_to_png_api(svg_path, png_path, viewport, scale)
    except ImportError:
        print(f"  (playwright not importable as a Python module — "
              f"falling back to the CLI, no {scale}x scaling)", file=sys.stderr)
        _svg_to_png_cli(svg_path, png_path, viewport)

# ------------------------------------------------------------ modes ---

def run_full(args):
    svg = ebs.build_diagram(width=args.width, height=args.height)
    with open(args.output, "w") as f:
        f.write(svg)
    print(f"Wrote {args.output}")

def run_sequence(args):
    svg_paths = ebs.render_sequence(args.ids, width=args.width, height=args.height)
    print(f"Wrote {len(svg_paths)} stage SVGs: {', '.join(svg_paths)}")

    print("Rendering PNGs...")
    png_paths = []
    for svg_p in svg_paths:
        png_p = svg_p.replace(".svg", ".png")
        svg_to_png(svg_p, png_p, viewport=(args.viewport_w, args.viewport_h), scale=args.scale)
        png_paths.append(png_p)
        print(f"  {svg_p} -> {png_p}")

    print("Assembling GIF...")
    from PIL import Image
    frames = [Image.open(p).convert("RGBA") for p in png_paths]
    flat_frames = []
    for f in frames:
        bg = Image.new("RGB", f.size, (255, 255, 255))
        bg.paste(f, mask=f.split()[3])
        flat_frames.append(bg)

    durations = [args.frame_ms] * (len(flat_frames) - 1) + [args.hold_last_ms]
    flat_frames[0].save(
        args.output, save_all=True, append_images=flat_frames[1:],
        duration=durations, loop=0, optimize=False,
    )
    print(f"Wrote {args.output} ({len(flat_frames)} frames)")

    if not args.keep_pngs:
        for p in png_paths:
            os.remove(p)
    print(f"Individual stage SVGs kept: {', '.join(svg_paths)}")

# ---------------------------------------------------------------- CLI --

def main():
    parser = argparse.ArgumentParser(description="Generate the energy-budget diagram, full or staged.")
    sub = parser.add_subparsers(dest="mode", required=True)

    p_full = sub.add_parser("full", help="generate the complete diagram as one SVG")
    p_full.add_argument("-o", "--output", default="diagram.svg")
    p_full.add_argument("--width", type=int, default=800)
    p_full.add_argument("--height", type=int, default=980)
    p_full.set_defaults(func=run_full)

    p_seq = sub.add_parser("sequence", help="generate a cumulative staged sequence as a GIF")
    p_seq.add_argument("ids", nargs="+", help="segment ids in reveal order, e.g. potential radiated dissipated")
    p_seq.add_argument("-o", "--output", default="sequence.gif")
    p_seq.add_argument("--width", type=int, default=800)
    p_seq.add_argument("--height", type=int, default=980)
    p_seq.add_argument("--viewport-w", type=int, default=900)
    p_seq.add_argument("--viewport-h", type=int, default=1100)
    p_seq.add_argument("--scale", type=int, default=2, help="render scale (Python API only, ignored by CLI fallback)")
    p_seq.add_argument("--frame-ms", type=int, default=900, help="duration of each non-final frame")
    p_seq.add_argument("--hold-last-ms", type=int, default=2500, help="duration the final frame holds")
    p_seq.add_argument("--keep-pngs", action="store_true", help="keep intermediate PNGs (deleted by default)")
    p_seq.set_defaults(func=run_sequence)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()