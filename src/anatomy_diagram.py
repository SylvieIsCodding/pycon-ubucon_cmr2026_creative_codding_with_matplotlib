"""
Bonus -- the Figure / Axes anatomy diagram.

Used early in the talk to demystify matplotlib's object model before the
demo even starts: everything lives inside a Figure, and the Axes is where
the actual plotting happens.

Run:
    python src/anatomy_diagram.py
Output:
    output/anatomy_diagram.png
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"

fig, ax = plt.subplots(figsize=(9, 6))
x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x) * 0.5 + 1, color="#0B3D62", linewidth=2.5)
ax.set_title("Axes Title", fontsize=13)
ax.set_xlabel("X Label", fontsize=11)
ax.set_ylabel("Y Label", fontsize=11)
ax.grid(alpha=0.3)


def annotate(text, xy, xytext, color="#E8792C"):
    ax.annotate(
        text, xy=xy, xytext=xytext,
        xycoords="figure fraction", textcoords="figure fraction",
        fontsize=12, color=color, fontweight="bold", ha="center",
        arrowprops=dict(arrowstyle="->", color=color, lw=1.6),
    )


# Label the Figure itself with a dashed border around the whole canvas.
fig.text(0.02, 0.97, "Figure", fontsize=15, fontweight="bold", color="#E8792C")
fig.patches.append(
    plt.Rectangle((0.01, 0.01), 0.98, 0.94, transform=fig.transFigure,
                  fill=False, edgecolor="#E8792C", linewidth=2.5, linestyle="--")
)

annotate("Axes\n(the plotting area)", (0.5, 0.55), (0.82, 0.15))
annotate("Spine", (0.135, 0.5), (0.05, 0.3))
annotate("Tick", (0.2, 0.135), (0.05, 0.05))

OUTPUT_DIR.mkdir(exist_ok=True)
out_path = OUTPUT_DIR / "anatomy_diagram.png"
fig.savefig(out_path, dpi=200, facecolor="white")
print(f"Saved {out_path}")
