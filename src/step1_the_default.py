"""
Step 1 -- The honest default.

ax.bar() once, done. Default blue, boxed spines, a full grid, a generic
title. This is the chart most of us have shipped at some point -- and
there's nothing *wrong* with it. It's just unconsidered.

Run:
    python src/step1_the_default.py
Output:
    output/step1_the_default.png
"""

from pathlib import Path
import matplotlib.pyplot as plt

from data import months, temp

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"

fig, ax = plt.subplots(figsize=(12.8, 7.2))

# One call. Default color, default width, default everything.
ax.bar(months, temp)

ax.set_title("Average Monthly Temperature - Yaounde")
ax.set_ylabel("Temperature (C)")
ax.grid(True, axis="y")

fig.tight_layout()

OUTPUT_DIR.mkdir(exist_ok=True)
out_path = OUTPUT_DIR / "step1_the_default.png"
fig.savefig(out_path, dpi=150)
print(f"Saved {out_path}")
