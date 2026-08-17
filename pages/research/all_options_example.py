"""
all_options_example.py

The rule: a Ring B image renders ONLY when its own id is called (appears
in SEQUENCE_IDS), and ONLY if SHOW_IMAGES is True. One flag. If an id in
SEQUENCE_IDS has no entry in MASTER_IMAGES, it just never shows an image —
no error, nothing to configure per-id.

Output layout: everything lands under OUTPUT_DIR, sorted into svg/, png/,
and gif/ subfolders (created automatically). Every SVG also gets a matching
PNG by default — PNG is the safe format for pasting into PowerPoint, which
is known to scramble/mangle SVGs.

Edit MASTER_IMAGES below to point each Ring B id at its real file — every
entry currently repeats dummy.png as a placeholder.
"""

from pathlib import Path
import energy_budget_svg as e

HERE = Path(__file__).resolve().parent
DUMMY = HERE / "dummy.png"
if not DUMMY.exists():
    raise FileNotFoundError(
        f"Expected dummy.png next to this script at: {DUMMY}\n"
        f"Generate one with the PIL snippet in README.md's 'Images' section, "
        f"or point DUMMY at any image you already have."
    )
DUMMY = str(DUMMY)

OUTPUT_DIR = str(HERE / "output")   # -> output/svg/, output/png/, output/gif/

# --- Master image list: every Ring B id, one line each. Edit the path on ---
# --- the right per id as needed; leave an id out entirely to never show it.
MASTER_IMAGES = {
    'source_ground':     DUMMY,
    'tsunami':            DUMMY,
    'friction':           DUMMY,
    'offfault_damage':    DUMMY,
    'longterm_viscous':   DUMMY,
    'constant_rate':      DUMMY,
    'tidal':              DUMMY,
    'hydrological':       DUMMY,
    'transient':          DUMMY,
    'fault_interaction':  DUMMY,
}
e.SEGMENT_IMAGES.update(MASTER_IMAGES)
e.CENTER_IMAGE = DUMMY

# --- The one flag ---
SHOW_IMAGES = True   # False = no Ring B images render at all, regardless of MASTER_IMAGES

# --- The sequence to render. Only ids listed here can ever show an image —
# --- an id in MASTER_IMAGES that's NOT in SEQUENCE_IDS never appears. ---
SEQUENCE_IDS = ['potential', 'radiated', 'dissipated', 'offfault_damage', 'source_ground']


# ============================================================================
# 1. Full diagram — every Ring B id that's ever going to matter, fully
#    highlighted, images shown per SHOW_IMAGES. SVG + matching PNG.
# ============================================================================
svg1 = e.build_diagram(
    highlight_B=set(SEQUENCE_IDS) & e.ALL_IDS_B,
    show_images=(set(SEQUENCE_IDS) & set(MASTER_IMAGES)) if SHOW_IMAGES else None,
)
svg1_path, png1_path = e.save_diagram(svg1, 'opt_1_full', base_dir=OUTPUT_DIR)

# ============================================================================
# 2. Sequential (staged) rendering — images_follow_sequence ties each image
#    to the exact stage its own id is called, per SHOW_IMAGES.
#    Every stage gets both an SVG and a matching PNG automatically.
# ============================================================================
svg_paths, png_paths = e.render_sequence(
    SEQUENCE_IDS, prefix='opt_2_seq_',
    images_follow_sequence=SHOW_IMAGES,
    base_dir=OUTPUT_DIR,
)

# ============================================================================
# 3. GIF version of 2. (Reuses the PNGs render_sequence already made — no
#    duplicate rendering.)
# ============================================================================
gif3_path = e.render_gif(
    SEQUENCE_IDS, gif_name='opt_3_sequence', prefix='opt_3_seq_',
    images_follow_sequence=SHOW_IMAGES,
    base_dir=OUTPUT_DIR,
)

# ============================================================================
# 4. Step 3, center replaced by an IMAGE.
# ============================================================================
gif4_path = e.render_gif(
    SEQUENCE_IDS, gif_name='opt_4_sequence_center_image', prefix='opt_4_seq_',
    images_follow_sequence=SHOW_IMAGES,
    show_center_image=True,
    base_dir=OUTPUT_DIR,
)

# ============================================================================
# 5. Step 3, center replaced by TEXT.
# ============================================================================
gif5_path = e.render_gif(
    SEQUENCE_IDS, gif_name='opt_5_sequence_center_text', prefix='opt_5_seq_',
    images_follow_sequence=SHOW_IMAGES,
    center_text=['Fault', 'Energy Budget'],
    base_dir=OUTPUT_DIR,
)

# ============================================================================
# 6. background_color — None (default) stays transparent; any CSS color
#    gives an opaque background sized exactly to the auto-computed crop.
# ============================================================================
svg6 = e.build_diagram(background_color='#FFFFFF')
svg6_path, png6_path = e.save_diagram(svg6, 'opt_6_background_white', base_dir=OUTPUT_DIR)

print(f"Done. Output under: {OUTPUT_DIR}/{{svg,png,gif}}/")
print(f"  1: {svg1_path}  +  {png1_path}")
print(f"  2: {len(svg_paths)} staged SVGs + {len(png_paths)} matching PNGs")
print(f"  3: {gif3_path}")
print(f"  4: {gif4_path}")
print(f"  5: {gif5_path}")
print(f"  6: {svg6_path}  +  {png6_path}")
