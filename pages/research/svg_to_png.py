#!/usr/bin/env python3
"""
svg_to_png.py — convert SVG files to PNG via real Chromium.

Exists as its own step because ImageMagick's SVG rendering (and wkhtmltoimage,
and macOS's sips/Preview) have all been confirmed to mishandle textPath and
marker elements on this diagram — silently dropping curved labels or arrows
rather than erroring. This script only does rasterization; hand the PNGs to
ImageMagick (or anything else) for GIF assembly, compositing, etc.

Rendering itself is delegated to energy_budget_svg.svg_to_png() — the single
canonical implementation (Playwright Python API, falling back automatically
to the `playwright` CLI if the API isn't importable, e.g. under a `pipx`
install). Kept in one place so this script and master.py can't drift out of
sync with each other, which happened once during development.

Usage:
    python3 svg_to_png.py stage*.svg
    python3 svg_to_png.py stage*.svg --scale 3 --viewport 900x1100
"""

import argparse
import glob
import os
import sys

import energy_budget_svg as ebs


def convert(svg_paths, viewport=(900, 1100), scale=2):
    png_paths = []
    for svg_path in svg_paths:
        png_path = os.path.splitext(svg_path)[0] + ".png"
        ebs.svg_to_png(svg_path, png_path, viewport=viewport, scale=scale)
        png_paths.append(png_path)
        print(f"  {svg_path} -> {png_path}")
    return png_paths


def main():
    parser = argparse.ArgumentParser(description="Convert SVG files to PNG via headless Chromium.")
    parser.add_argument("svgs", nargs="+", help="SVG file paths or globs (e.g. 'stage*.svg')")
    parser.add_argument("--viewport", default="900x1100", help="WIDTHxHEIGHT, default 900x1100")
    parser.add_argument("--scale", type=int, default=2, help="device scale factor, default 2")
    args = parser.parse_args()

    # expand any globs the shell didn't already expand (e.g. if quoted)
    svg_paths = []
    for pattern in args.svgs:
        matches = sorted(glob.glob(pattern))
        svg_paths.extend(matches if matches else [pattern])

    missing = [p for p in svg_paths if not os.path.isfile(p)]
    if missing:
        print(f"Error: file(s) not found: {missing}", file=sys.stderr)
        sys.exit(1)

    w, h = (int(x) for x in args.viewport.lower().split("x"))
    print(f"Converting {len(svg_paths)} file(s) at {w}x{h} @ {args.scale}x scale...")
    convert(svg_paths, viewport=(w, h), scale=args.scale)
    print("Done.")


if __name__ == "__main__":
    main()