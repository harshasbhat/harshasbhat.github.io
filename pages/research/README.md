# Energy Budget Diagram

A generator for the fault energy-budget radial diagram — `Observable Potential
Energy = Radiated + Dissipated` — as clean, editable, self-contained SVG.
Produces a full diagram, a cumulative staged sequence (individual SVGs), or
an animated GIF of that sequence, with independent control over highlighting,
per-segment images, center content, and canvas cropping.

## Files

| File | Purpose |
|---|---|
| `energy_budget_svg.py` | Core library. Everything lives here. |
| `all_options_example.py` | **The reference.** Every option, demonstrated and tested. Start here for usage. |
| `svg_to_png.py` | Standalone SVG→PNG converter, usable on its own outside the diagram pipeline. |

All three (or just the two you need) should sit in the same folder.

There is no CLI anymore (an earlier `master.py` was retired) — the parameter
space includes dicts and sets (image registries, per-id timing) that don't
map cleanly onto command-line flags, so Python is the actual interface.

## Installation

```bash
pip3 install matplotlib pillow playwright
playwright install chromium
```

- `playwright install chromium` is a **separate required step** — without it
  you'll get `Executable doesn't exist`, not a helpful error.
- **Homebrew Python on macOS**: `pip3 install` may refuse with
  `externally-managed-environment`. Fix: `pip3 install --break-system-packages ...`,
  or a venv if you prefer the "correct" route.
- **Multiple Python installs (common on Mac)**: if you install with `pip3`
  but run scripts with a different `python3` (e.g. VS Code's selected
  interpreter, or `/usr/bin/python3` vs Homebrew's), the install won't be
  visible to the interpreter actually running your code. Check with
  `which python3` / `which pip3` — if they print different paths, that's
  the mismatch. In VS Code specifically: Cmd+Shift+P → "Python: Select
  Interpreter" → pick the one matching where you installed Playwright.
- **If Playwright was installed via `pipx`**, `import playwright` fails from
  a plain script even though the `playwright` CLI command works — `pipx`
  isolates it. The library's `svg_to_png()` detects this automatically and
  falls back to the CLI. One real cost: the CLI fallback can't do >1x scale
  (no `--device-scale-factor` flag), so you'll get 1x renders until
  Playwright is also `pip install`-able for your actual interpreter.

## Quick start

```python
import energy_budget_svg as e

# Full diagram -> writes svg/diagram.svg AND a matching png/diagram.png
svg = e.build_diagram()
e.save_diagram(svg, 'diagram')

# A cumulative staged sequence -> svg/stage01_potential.svg... + matching PNGs
svg_paths, png_paths = e.render_sequence(['potential', 'radiated', 'dissipated'])

# Same sequence, assembled into a GIF -> gif/sequence.gif
e.render_gif(['potential', 'radiated', 'dissipated'], gif_name='sequence')
```

Everything lands under `svg/`, `png/`, `gif/` in the current directory by
default — see **Output directories & automatic PNG** below.

## Valid segment ids

Pulled from `ALL_IDS_A` / `ALL_IDS_B` in the code — always matches what's
actually accepted; any other id raises `ValueError`.

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
| `constant_rate` | Constant Stress / Plate Rate | Potential *(dashed/empty — assumed, not directly studied)* |
| `tidal` | Tidal | Potential |
| `hydrological` | Hydrological | Potential |
| `transient` | Transient | Potential |
| `fault_interaction` | Fault Interaction | Potential |

"Sits under" is visual placement only — no functional link. Highlighting a
Ring B id does **not** auto-highlight its Ring A parent, or vice versa; each
ring's highlight set is independent, by design.

## `build_diagram()` — every parameter

```python
def build_diagram(width=800, height=980, highlight_A=None, highlight_B=None,
                   center_image=None, show_center_image=False, show_images=None,
                   show_center=True, center_text=None,
                   highlight_grow_pct=0.25, dim_shrink_pct=0.15,
                   force_viewbox=None, return_bounds=False,
                   background_color=None)
```

| Parameter | Default | What it does |
|---|---|---|
| `width`, `height` | `800`, `980` | Only affects internal layout math — the **output canvas is auto-cropped** to actual content regardless (see below), so these rarely need changing. |
| `highlight_A` | `None` | Set of Ring A ids to keep at full brightness (`None` = everyone full brightness, no dimming at all). |
| `highlight_B` | `None` | Same, for Ring B. Fully independent of `highlight_A`. |
| `highlight_grow_pct` | `0.25` | How far a **highlighted** wedge's outer edge pops outward, as a fraction of its ring's thickness. |
| `dim_shrink_pct` | `0.15` | How far a **dimmed** wedge's outer edge pulls inward, as a fraction of ring thickness. |
| `show_images` | `None` | Set of Ring B ids whose registered image (from `SEGMENT_IMAGES`) should render. Independent of `highlight_B` — a segment can be highlighted without its image, or show its image while dimmed. |
| `show_center` | `True` | Master on/off for the center hub's content. `False` = completely blank, overrides everything else below. |
| `center_text` | `None` | String or list of strings. If given, **always wins** — shows this text regardless of any image requested. |
| `center_image` | `None` | Explicit image path override — wins over `show_center_image`/`CENTER_IMAGE`, but loses to `center_text`. |
| `show_center_image` | `False` | If `True` (and neither `center_text` nor `center_image` given), shows `CENTER_IMAGE` from the registry. |
| `background_color` | `None` | `None` = transparent (default). Any CSS color = an opaque rect sized exactly to the auto-cropped canvas. |
| `force_viewbox` | `None` | `(vb_x, vb_y, vb_size)` — skips auto-crop, uses this fixed box instead. This is how `render_sequence` keeps every stage in a GIF the same size; not usually something you set directly. |
| `return_bounds` | `False` | If `True`, returns `(svg_string, (vb_x, vb_y, vb_size))` instead of just the SVG — lets you find out how big a configuration needs without necessarily using that render. |

**Precedence for the center, most specific wins:**
`show_center=False` > `center_text` > `center_image` > `show_center_image` (registry) > default text.

## Output directories & automatic PNG

PowerPoint is known to scramble/mangle pasted SVGs — dropped text, broken
curves, wrong colors. So every SVG this library writes gets a matching PNG
by default (the safe format for slides), and outputs are sorted into three
subfolders rather than left flat:

```
base_dir/
├── svg/
├── png/
└── gif/
```

All three are created automatically. Three functions write here:

```python
e.save_diagram(svg_content, name, base_dir='.', also_png=True, scale=2)
# -> (svg_path, png_path). For ONE diagram (not a sequence).

e.render_sequence(ids, base_dir='.', also_png=True, png_scale=2, prefix='stage', ...)
# -> (svg_paths, png_paths), both lists, same order as `ids`.

e.render_gif(ids, gif_name='sequence', base_dir='.', prefix='stage', ...)
# -> gif_path. Reuses render_sequence's own PNGs rather than rendering twice.
```

**Filename collision gotcha, worth knowing before it bites you:** files are
named `f"{prefix}{stage:02d}_{id}"` — so two calls collide only if they
produce the *same* filenames, which happens when they share both `prefix`
**and** the same `ids` at the same stage positions. If you call
`render_sequence`/`render_gif` **more than once with the same `ids` list**
into the same `base_dir`, give each call a **different `prefix`** —
otherwise the second call's files silently overwrite the first's, no error.
This happened once during development: three `render_gif()` calls all using
the *same* `SEQUENCE_IDS` list, sharing the default `prefix='stage'`, all
wrote to the same `svg/stage01_potential.svg` etc., and only the last
call's files survived. `all_options_example.py` gives each of its three
GIF-producing scenarios its own prefix (`opt_3_seq_`, `opt_4_seq_`,
`opt_5_seq_`) for exactly this reason — verified by confirming the second
call's content actually differs from and replaces the first's.

Turn off the automatic PNG if you don't want it: `also_png=False` on
`save_diagram`/`render_sequence`, or `keep_pngs=False` on `render_gif` (which
still *renders* PNGs internally — it needs them to build the GIF — but
deletes them afterward instead of leaving them in `png/`).


Two places an image can go: **outside a Ring B wedge**, or **in the center**
(replacing the default text). Both work off a **registry** — registering an
image and *showing* it are separate steps on purpose:

```python
import energy_budget_svg as e

e.SEGMENT_IMAGES['friction'] = '/path/to/photo.jpg'   # register, doesn't show it yet
e.CENTER_IMAGE = '/path/to/center.jpg'

e.build_diagram(show_images={'friction'})               # now it shows
e.build_diagram(show_center_image=True)                  # center image shows
```

Registering an id with no corresponding image is a silent no-op, not an
error — requesting `show_images={'tidal'}` when `tidal` was never registered
just shows nothing for it.

**Images embed as base64 data URIs**, not external file links — the SVG
stays fully self-contained and portable, at the cost of file size scaling
with image size (matters most for GIF sequences, where every stage re-embeds
the same image).

**Square vs. non-square source images:** a square image fills the circular
crop exactly, with only its four corners rounded off — no content lost. A
non-square image gets center-cropped to fill the box first
(`preserveAspectRatio="xMidYMid slice"`), *then* circularly clipped — that's
where you'd actually lose edges.

### Images in a sequence — `images_follow_sequence`

The simple case: **one flag**, no per-id timing to configure. A Ring B
image appears starting exactly at the stage where its own id is first
called in the sequence list — the same moment its wedge gets highlighted.

```python
e.SEGMENT_IMAGES['offfault_damage'] = 'photo.jpg'
e.SEGMENT_IMAGES['source_ground'] = 'photo2.jpg'

ids = ['potential', 'radiated', 'dissipated', 'offfault_damage', 'source_ground']
svg_paths, png_paths = e.render_sequence(ids, images_follow_sequence=True)
# offfault_damage's image appears at stage 4 (its own position), stays through 5.
# source_ground's image appears at stage 5. Nothing before that, for either.
# Any id registered but NOT in `ids` never shows an image, no matter what.
```

For finer control — an image on a *different* stage than its own id's —
`show_images_from={'friction': 4}` (1-indexed stage numbers) is the escape
hatch, ignored when `images_follow_sequence=True`.

## Arrows

Any Ring B segment dict can carry a radial arrow:

```python
{'id': 'friction', 'label': 'Friction', 'color': DIS, 'arrow': 'out'}
```

`'in'` points toward the center, `'out'` points away, `'both'` gets
arrowheads on each end, omit the key for no arrow. Per-segment overrides:
`arrow_color`, `arrow_width`, `arrow_head_size`, `arrow_r_in`, `arrow_r_out`.

## Canvas: auto-crop, not a fixed size

The SVG's `viewBox` is computed from **actual content** — the furthest
wedge, arrow, or image reaches from center, plus small padding — not a
fixed canvas. A plain diagram crops tighter than one with a popped wedge
and an image hanging off it.

**Sequences are the one place this needs care, and it's handled
automatically**: every stage in a `render_sequence()`/`render_gif()` run
shares **one** canvas size, computed once from the *final* (fullest) stage.
Auto-cropping each stage to its own content would make GIF frames different
sizes and the diagram would visibly jump around during playback — this is
a real bug that was caught and fixed during development, not a
hypothetical. If you ever call `build_diagram(force_viewbox=...)` directly
with a mismatched box, you'd reintroduce it.

## Rendering: why Playwright/Chromium specifically

Tested, not assumed. Every other SVG renderer tried on this exact diagram
(curved `textPath` labels + arrow/image `marker`/`clipPath` elements) failed
in some way:

| Tool | Result |
|---|---|
| ImageMagick (`convert`) | Fails outright without a working `rsvg-convert` delegate |
| `wkhtmltoimage` | Silently drops **every** curved label |
| `cairosvg` | Renders labels correctly, but got a plain text color wrong — a rendering bug, not a font issue |
| macOS `sips` / Preview / Quick Look | Confirmed unreliable — dropped text earlier in development, and separately showed apparent aspect-ratio/sizing quirks even on a file independently verified (by hand-computed geometry) to be a perfect square |
| **Playwright (real Chromium)** | **Correct, every time**, across dozens of checks |

If you ever see something look wrong in Preview/QuickLook specifically,
check it in an actual browser (Safari, Chrome) before assuming the file is
broken — QuickLook's rendering engine has already been wrong twice in ways
a real browser wasn't.

## `all_options_example.py` — what each scenario shows

Run it as-is (uses `dummy.png`, generated automatically if missing) or copy
sections into your own script.

1. Full diagram, all rings shown, both with and without images
2. Cumulative staged sequence, images tied to their own id via `images_follow_sequence`
3. GIF version of 2
4. Same GIF, center replaced by an image
5. Same GIF, center replaced by custom text
6. `background_color` — transparent (default) vs. an opaque fill

`MASTER_IMAGES` at the top of that file is a template — one line per Ring B
id, all pointing at `dummy.png` — edit individual paths as needed. The one
flag controlling whether any of them actually show is `SHOW_IMAGES`.

All output lands under `output/{svg,png,gif}/` next to the script (its
`OUTPUT_DIR` constant) — 22 SVGs, 22 matching PNGs, 3 GIFs, one non-colliding
set per scenario (see the filename collision note above — this file is why
that note exists).

## Known limitations

- GIF assembly flattens transparency onto **white** — GIF has no real alpha
  compositing across frames. A dark-background version would need that
  flatten color to become a parameter (or use `background_color` on the SVG
  itself before rasterizing, which sidesteps the issue).
- The Playwright CLI fallback (triggered under `pipx`-only installs) can't
  do >1x render scaling.
- Registering an image and showing it are deliberately separate — if
  something "isn't appearing," check both: is it in `SEGMENT_IMAGES`
  (or `CENTER_IMAGE`), AND is it actually requested via `show_images`/
  `show_center_image`/`images_follow_sequence`?
- `force_viewbox` exists mainly for `render_sequence`'s internal use. Setting
  it by hand on a standalone `build_diagram()` call will skip auto-crop
  entirely — fine if intentional, easy to forget if not.
