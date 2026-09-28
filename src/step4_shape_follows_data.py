"""
Step 4 -- Let the shape follow the data.

Each bar becomes a petal. Length and color still read straight off the same
twelve numbers -- no new data, just a different geometry. This is the one
genuinely new function in the whole demo: `petal()`. Everything before it
was subtraction and mapping.

    DATA  ->  PARAMETERS  ->  VISUAL RULES  ->  ARTISTIC OUTPUT
    temp      petal length    petal(): a lens    a flower
              petal color     shape + a ripple

What changed vs. Step 3:
    - removed: ax.bar()
    - added:   petal() -- returns the outline of one petal
    - added:   ax.fill() draws that outline, colored by temp_cmap()

Run:
    python src/step4_shape_follows_data.py
Output:
    output/step4_shape_follows_data.png
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

from data import months, temp, NAVY_DARK, normalize, temp_cmap

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"


def petal(theta_c, r_in, r_out, half_w, n=80, wobble=0.015, freq=3, seed=0):
    """
    Outline of one petal, as (angle, radius) arrays for a polar Axes.

    theta_c -- the angle the petal points toward (its center line)
    r_in    -- radius where the petal starts (it closes cleanly here)
    r_out   -- radius of the petal tip; this is where your data goes
    half_w  -- half the petal's angular width
    n       -- how many points describe the outline
    wobble  -- size of a small ripple, so petals feel organic, not mechanical
    freq    -- how fast the ripple oscillates
    seed    -- gives each petal its own ripple; same seed, same petal every run
    """
    t = np.linspace(-1, 1, n)
    angle = theta_c + t * half_w

    # cos() is 1 at the center of the petal and 0 at both edges, so the
    # outline swells out to r_out and pinches back to r_in on each side.
    envelope = np.cos(t * np.pi / 2)
    radius = r_in + (r_out - r_in) * envelope

    if wobble > 0:
        phase = np.random.default_rng(seed).uniform(0, 2 * np.pi)
        ripple = wobble * (0.65 * np.sin(freq * t * np.pi + phase)
                           + 0.35 * np.sin(2 * freq * t * np.pi + phase * 1.6))
        radius = radius + ripple * envelope  # the envelope keeps the edges pinned

    return angle, radius


def main():
    fig = plt.figure(figsize=(10, 10))
    fig.patch.set_facecolor(NAVY_DARK)
    ax = fig.add_subplot(projection="polar")
    ax.set_facecolor(NAVY_DARK)

    theta = np.linspace(0, 2 * np.pi, 12, endpoint=False)
    half_w = (2 * np.pi / 12) * 0.42
    r_in = 0.16
    temp_out = r_in + normalize(temp, 0.22, 0.58)  # temperature -> petal length

    for i in range(12):
        a, r = petal(theta[i], r_in, temp_out[i], half_w, seed=i)
        ax.fill(a, r, color=temp_cmap(temp[i]), alpha=0.95, zorder=3)

    for i, month in enumerate(months):
        ax.text(theta[i], temp_out[i] + 0.08, month, ha="center", va="center",
                fontsize=12, color="#D9E4EC")

    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.set_xticks([])
    ax.set_yticklabels([])
    ax.set_ylim(0, 1.0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.grid(False)

    fig.tight_layout()

    OUTPUT_DIR.mkdir(exist_ok=True)
    out_path = OUTPUT_DIR / "step4_shape_follows_data.png"
    fig.savefig(out_path, dpi=150, facecolor=NAVY_DARK)
    print(f"Saved {out_path}")


# Step 5 imports petal() from this file, so the drawing only runs when this
# file is executed directly -- not when it's imported.
if __name__ == "__main__":
    main()
