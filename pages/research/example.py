import research as e

svg = e.build_diagram()          # full diagram, nothing dimmed
with open("full.svg", "w") as f:
    f.write(svg)


svg = e.build_diagram(
    highlight_A={'dissipated'},
    highlight_B={'friction', 'offfault_damage'},
)
with open("highlight_test.svg", "w") as f:
    f.write(svg)    

ids = ['potential', 'radiated', 'dissipated', 'offfault_damage', 'source_ground']
paths = e.render_sequence(ids)
