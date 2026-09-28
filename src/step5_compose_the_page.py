"""
Step 5 -- Compose the page.

The shape doesn't change again here -- only what surrounds it does. Rainfall
comes in as a second, translucent layer of petals (the same petal() function
from Step 4, called again with different numbers), and the title moves to the
center of the circle instead of sitting above the chart.
This is composition, not decoration.

What changed vs. Step 4:
    - added: rainfall as a soft outer petal behind each temperature petal
    - added: fig.text() -- the title lives in the middle of the bloom
    - added: a faint glow behind the bloom, and a small highlight petal
             inside each temperature petal for a bit of depth
    - changed: upper-case month labels, pushed out past the rainfall layer

Run:
    python src/step5_compose_the_page.py
Output:
    output/step5_compose_the_page.png
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

from data import months, temp, rain, NAVY_DARK, ICEBLUE, LIME, YELLOW, normalize, temp_cmap
from step4_shape_follows_data import petal  # the same function as Step 4

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"

fig = plt.figure(figsize=(11, 11))
fig.patch.set_facecolor(NAVY_DARK)
ax = fig.add_subplot(projection="polar")
ax.set_facecolor(NAVY_DARK)

# A soft glow: a few stacked, nearly transparent discs behind everything.
circle = np.linspace(0, 2 * np.pi, 200)
for radius, alpha in zip(np.linspace(1.2, 0.55, 12), np.linspace(0.015, 0.05, 12)):
    ax.fill(circle, np.full(200, radius), color=YELLOW, alpha=alpha, zorder=0)

theta = np.linspace(0, 2 * np.pi, 12, endpoint=False)
half_w = (2 * np.pi / 12) * 0.44
r_in = 0.30
temp_out = r_in + normalize(temp, 0.24, 0.58)         # temperature -> petal length
rain_out = temp_out + normalize(rain, 0.05, 0.28)     # rainfall -> the layer beyond it

for i in range(12):
    # Layer 1 (back): rainfall, a wider, translucent petal.
    a, r = petal(theta[i], r_in, rain_out[i], half_w * 1.4,
                 n=90, wobble=0.018, freq=2, seed=i + 50)
    ax.fill(a, r, color=ICEBLUE, alpha=0.22, zorder=1)

    # Layer 2: temperature, colored from the data (same as Step 4).
    a, r = petal(theta[i], r_in, temp_out[i], half_w,
                 n=90, wobble=0.012, freq=3, seed=i)
    ax.fill(a, r, color=temp_cmap(temp[i]), alpha=0.95, zorder=3,
            edgecolor=NAVY_DARK, linewidth=0.6)

    # Layer 3 (front): a small, faint highlight for depth.
    a, r = petal(theta[i], r_in, r_in + (temp_out[i] - r_in) * 0.5, half_w * 0.55,
                 n=40, wobble=0.006, freq=4, seed=i + 100)
    ax.fill(a, r, color="white", alpha=0.10, zorder=4)

for i, month in enumerate(months):
    ax.text(theta[i], rain_out[i] + 0.09, month.upper(), ha="center", va="center",
            fontsize=11.5, fontweight="bold", color="#CFE0EC", alpha=0.85)

ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.set_xticks([])
ax.set_yticklabels([])
ax.set_ylim(0, 1.28)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.grid(False)

fig.tight_layout()

# The title goes in the empty middle of the bloom. (0.5, 0.5) is the center
# of the figure, which is also the center of this polar Axes.
fig.text(0.5, 0.5 + 0.018, "YAOUNDÉ", ha="center", va="center",
         fontsize=17, fontweight="bold", color="white", alpha=0.95)
fig.text(0.5, 0.5 - 0.018, "one year, one bloom", ha="center", va="center",
         fontsize=9, style="italic", color=LIME, alpha=0.9)

OUTPUT_DIR.mkdir(exist_ok=True)
out_path = OUTPUT_DIR / "step5_compose_the_page.png"
fig.savefig(out_path, dpi=150, facecolor=NAVY_DARK)
print(f"Saved {out_path}")
