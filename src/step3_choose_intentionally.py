"""
Step 3 -- Choose intentionally.

Every month earns its own color, mapped straight from its temperature
instead of a default cycle -- cool blue for the coolest months, warm orange
for the hottest. Color is now a second channel carrying the same data, so
you can read the seasons without a single axis label.

What changed vs. Step 2:
    - added:   color=temp_cmap(temp[i]) -- one color per bar, from the data
    - changed: a dark canvas, so the colors read as light
    - changed: month labels are placed with ax.text() just outside the bars

Run:
    python src/step3_choose_intentionally.py
Output:
    output/step3_choose_intentionally.png
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

from data import months, temp, NAVY_DARK, normalize, temp_cmap

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"

fig = plt.figure(figsize=(10, 10))
fig.patch.set_facecolor(NAVY_DARK)
ax = fig.add_subplot(projection="polar")
ax.set_facecolor(NAVY_DARK)

theta = np.linspace(0, 2 * np.pi, 12, endpoint=False)
width = 2 * np.pi / 12 * 0.72
inner = 0.30
height = normalize(temp, 0.10, 0.62)

for i in range(12):
    color = temp_cmap(temp[i])  # the data picks the color
    ax.bar(theta[i], height[i], width=width, bottom=inner, color=color)

for i, month in enumerate(months):
    ax.text(theta[i], 0.98, month, ha="center", va="center",
            fontsize=13, color="#E8EEF3")

ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.set_xticks([])
ax.set_yticklabels([])
ax.set_ylim(0, 1.05)

for spine in ax.spines.values():
    spine.set_visible(False)
ax.grid(color="#22394B", linewidth=0.6)

fig.tight_layout()

OUTPUT_DIR.mkdir(exist_ok=True)
out_path = OUTPUT_DIR / "step3_choose_intentionally.png"
fig.savefig(out_path, dpi=150, facecolor=NAVY_DARK)
print(f"Saved {out_path}")
