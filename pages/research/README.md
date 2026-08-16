# Energy Budget Diagram

A generator for the fault energy-budget radial diagram — `Observable Potential
Energy = Radiated + Dissipated` — as clean, editable SVG. Produces either the
full diagram or a cumulative staged sequence (for talks), the latter as
individual SVGs plus an assembled GIF.

## Files

| File | Purpose |
|---|---|
| `energy_budget_svg.py` | Core library. All diagram logic lives here — geometry, curved labels, arrows, highlight/dim staging, `render_sequence()`. |
| `master.py` | Command-line entry point. Wraps the library into two modes: `full` and `sequence`. **Start here.** |
| `svg_to_png.py` | Standalone SVG→PNG converter (Playwright/Chromium), usable on its own if you just want PNGs without the GIF step. |

`master.py` and `svg_to_png.py` both import `energy_budget_svg.py`, so all
three files need to stay in the same folder (or `energy_budget_svg.py` needs
to be on your `PYTHONPATH`).

## Installation

```bash
pip3 install matplotlib pillow playwright
playwright install chromium
```

Three notes that will save you time:

- **`playwright install chromium` is a separate, required step** — it downloads
  the actual browser binary. Skipping it gives a confusing
  `Executable doesn't exist` error, not a helpful one.
- **On modern macOS with Homebrew Python**, plain `pip3 install` may refuse
  with `externally-managed-environment`. Fixes, in order of preference: a
  virtualenv (`python3 -m venv .venv && source .venv/bin/activate`), `pipx`,
  or `pip3 install --break-system-packages ...` as a last resort.
- **If you installed Playwright via `pipx`**, the `playwright` CLI command
  works globally, but `import playwright` from a plain `python3` script will
  likely fail — `pipx` isolates it. `master.py` and `svg_to_png.py` both
  detect this automatically and fall back to shelling out to the CLI, with
  one caveat: the CLI has no `--device-scale-factor` flag, so the fallback
  path always renders at 1x, not the 2–3x you'd get from the Python API.

## Quick start

**Full diagram, no dimming, one SVG:**
```bash
python3 master.py full -o diagram.svg
```

**Staged sequence for a talk — cumulative highlighting, individual SVGs kept, plus a GIF:**
```bash
python3 master.py sequence potential radiated dissipated offfault_damage source_ground -o sequence.gif
```
Each id in the list is revealed in order; everything from earlier stages
stays highlighted. This example produces:
`stage01_potential.svg`, `stage02_radiated.svg`, `stage03_dissipated.svg`,
`stage04_offfault_damage.svg`, `stage05_source_ground.svg`, and `sequence.gif`.

Useful flags for `sequence` mode:
```
--frame-ms 900          duration of each non-final frame (ms)
--hold-last-ms 2500      duration the final, fully-built frame holds (ms)
--scale 2                render scale — Python API path only, ignored by the CLI fallback
--viewport-w / --viewport-h   render viewport size
--keep-pngs               keep the intermediate PNGs (deleted by default)
```

## Valid segment ids

Pulled directly from the code (`ALL_IDS_A`, `ALL_IDS_B`), so this always
matches what `master.py sequence` will actually accept.

**Ring A — the three balance terms:**
| id | Label |
|---|---|
| `radiated` | Radiated Energy (E_R) |
| `dissipated` | Observable Dissipation (D_O) |
| `potential` | Observable Potential Energy |

**Ring B — the ten sub-channels:**
| id | Label | Sits under |
|---|---|---|
| `source_ground` | Source & Ground Motion | Radiated |
| `tsunami` | Tsunami & Far-Field Coupling | Radiated |
| `friction` | Friction | Dissipated |
| `offfault_damage` | Off-Fault Damage | Dissipated |
| `longterm_viscous` | Long-Term / Viscous Flow | Dissipated |
| `constant_rate` | Constant Stress / Plate Rate | Potential *(drawn dashed/empty — assumed, not directly studied)* |
| `tidal` | Tidal | Potential |
| `hydrological` | Hydrological | Potential |
| `transient` | Transient | Potential |
| `fault_interaction` | Fault Interaction | Potential |

The "sits under" column is purely visual placement (which Ring A wedge a Ring
B segment is drawn beneath) — there's no functional parent/child link.
Highlighting a Ring B id does **not** automatically light up its Ring A
parent, and vice versa; each ring's highlight set is independent, by design.
Any id not in these two lists raises `ValueError`.

## How highlighting/dimming works

`build_diagram(highlight_A=..., highlight_B=...)` takes two sets of ids
(or `None` for "everyone at full brightness"). Any segment on that ring whose
id is *not* in the set gets:

- desaturated + faded wedge fill (`dim_desat`, `dim_opacity`)
- faded label text (`dim_text_opacity`) — labels stay **visible but faded**,
  not hidden, so the full taxonomy is always legible
- its arrow hidden by default (`dim_arrows=True`) — override if you want faded
  arrows instead of none

`render_sequence(ids)` builds these sets incrementally: stage *N*'s highlight
set is the union of ids from stages 1..N, so each stage's call is just
`{id}`, not the running total — the function accumulates it for you.

## Arrows

Any Ring B segment can carry a radial arrow via `'arrow': 'in' | 'out' | 'both'`
in its segment dict (or omit the key for no arrow). `'in'` points toward the
center, `'out'` points away. Direction, color, width, head size, and radial
span are all overridable per segment — see `radial_arrow()` and the
`arrow_*` keys read in `build_ring()`.

## Rendering: why Playwright/Chromium specifically

This was tested, not assumed. Every other SVG renderer tried on this exact
diagram (curved `textPath` labels + arrow `marker`s) failed in some way:

| Tool | Result |
|---|---|
| ImageMagick (`convert`) | Fails outright without a working `rsvg-convert` delegate |
| `wkhtmltoimage` | Silently drops **every** curved label — looks plausible, is wrong |
| `cairosvg` | Renders curved labels correctly, but got the center label's color wrong (a rendering bug, not a font issue) |
| macOS `sips` / Preview / Quick Look | Not fully tested, but shares the same underlying ImageIO engine that dropped text earlier in development — expect similar failures |
| **Playwright (real Chromium)** | **Correct, every time**, across dozens of checks |

If you ever swap in a different SVG→PNG tool, re-verify against a diagram
that actually has curved labels and arrows before trusting it — a diagram
that "looks done" can still be silently wrong.

## Customizing the diagram itself

Inside `build_diagram()` in `energy_budget_svg.py`:

- **Ring boundaries** (`ringA_boundaries`, `ringB_boundaries`) are flat angle
  lists in degrees, e.g. `[0, 90, 180, 360]` → 3 segments. Negative angles
  work fine. Resize a wedge or add one by editing the array plus the matching
  segment dict — no geometry rewrite needed.
- **Colors, radii, fonts** — `POT`/`RAD`/`DIS` hex colors, `R_A0/R_A1`,
  `R_B0/R_B1`, `rAfont`/`rBfont` are all set near the top of the function.
- **Multi-line labels** — pass `'label': ['line one', 'line two']` instead of
  a string; lines stack radially, centered as a block, with reading order
  auto-corrected on the half of the circle where text direction flips.
- **`vpos`** (`'top' | 'mid' | 'bottom'`) controls a label's position relative
  to its own arc line; **`flip`** (`True`/`False`/`None`) overrides the
  automatic upright/upside-down direction detection when needed — mainly
  relevant right at the 90°/270° boundary, where auto-detection is ambiguous.
- **Background is transparent** by default (no `<rect>` fill) — add one back
  if you need a guaranteed-opaque background for a specific embed target.

## Known limitations

- GIF assembly flattens transparency onto **white** — GIF doesn't support
  real alpha compositing across frames. For a dark-background version, that
  flatten color would need to become a parameter.
- The Playwright CLI fallback path (triggered automatically under `pipx`
  installs) can't do >1x render scaling — only the Python API path can.
- Arrow marker `<defs>` are cleared at the start of every `build_diagram()`
  call so each SVG stays self-contained — if you ever refactor to skip that
  reset, multi-call scripts (like `render_sequence`) will silently produce
  SVGs with arrows referencing markers that don't exist in that file, which
  render as invisible arrowheads. (This exact bug happened once during
  development — it's why the reset is there.)
