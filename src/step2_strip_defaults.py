"""
Step 2 -- Strip the defaults.

Remove the box around the plot, quiet the grid down -- and question the
shape itself. The rectangle was a default too. A year loops back on itself
(December is followed by January), so we ask matplotlib for a circle.

What changed vs. Step 1:
    - removed: the boxed spines
    - quieter: the grid is now faint concentric rings
    - changed: the Axes is polar -- one argument, projection="polar"
    - changed: one flat, muted color instead of default blue

Nothing about the data changed.

Run:
    python src/step2_strip_defaults.py
Output:
    output/step2_strip_defaults.png
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

from data import months, temp, normalize

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"

fig = plt.figure(figsize=(10, 10))

# The Figure is the page. The Axes is what you draw on -- and its shape is
# a choice. Ask for a polar Axes and the same bars bend into a circle.
ax = fig.add_subplot(projection="polar")

# Twelve evenly spaced angles, one per month.
theta = np.linspace(0, 2 * np.pi, 12, endpoint=False)
width = 2 * np.pi / 12 * 0.72         # each bar fills 72% of its slice
inner = 0.35                           # leave a hole in the middle
height = normalize(temp, 0.25, 0.55)   # temperature -> bar length

ax.bar(theta, height, width=width, bottom=inner, color="#2B3A42", alpha=0.85)

ax.set_theta_zero_location("N")  # January at the top...
ax.set_theta_direction(-1)       # ...then clockwise, like a clock

ax.set_xticks(theta)
ax.set_xticklabels(months, fontsize=13, color="#333333")
ax.set_yticklabels([])           # no radial numbers
ax.set_ylim(0, 1.0)

for spine in ax.spines.values():
    spine.set_visible(False)
ax.grid(color="#DADADA", linewidth=0.6)

fig.tight_layout()

OUTPUT_DIR.mkdir(exist_ok=True)
out_path = OUTPUT_DIR / "step2_strip_defaults.png"
fig.savefig(out_path, dpi=150, facecolor="white")
print(f"Saved {out_path}")
