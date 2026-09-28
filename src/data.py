"""
Shared dataset for the demo: Yaoundé's monthly climate normals.

Two variables, twelve months -- average temperature and average rainfall.
Every step script imports from here, so the data never changes between
steps -- only the code that renders it does. That's the whole point of the
demo: same input, different intention.

Source: WorldClim climate normals (1970-2000) for Yaoundé, as tabulated by
populationreview.org, rounded to whole degrees / millimetres. For a
similarly-sourced, independently verifiable dataset, see the UEA Climatic
Research Unit's Cameroon page.

Want to try your own city? Replace `temp` and `rain` below with twelve
values each -- every step script will re-render around your data.
"""

import numpy as np
from matplotlib.colors import LinearSegmentedColormap

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Average monthly temperature, in degrees Celsius.
temp = np.array([24, 25, 25, 25, 24, 23, 23, 23, 23, 23, 24, 24], dtype=float)

# Average monthly rainfall, in millimetres.
rain = np.array([21, 49, 139, 182, 220, 160, 80, 112, 249, 299, 104, 22], dtype=float)

# Shared color palette (dark canvas from Step 3 onward).
NAVY_DARK = "#0E2135"
ICEBLUE = "#C9DAF8"
LIME = "#C2ED58"
YELLOW = "#FFE052"
ORANGE = "#FFAB40"

# Cool blue -> green -> yellow -> warm orange. Color follows temperature,
# not an arbitrary default cycle.
_TEMP_CMAP = LinearSegmentedColormap.from_list(
    "yaounde", ["#5AC8FA", LIME, YELLOW, ORANGE]
)
# Stretch the colormap slightly past the data so the coolest and hottest
# months don't sit at the very ends of the scale.
TEMP_RANGE = (temp.min() - 0.5, temp.max() + 0.5)


def normalize(values, lo, hi):
    """Rescale `values` linearly so the smallest maps to `lo` and the largest to `hi`."""
    values = np.asarray(values, dtype=float)
    span = values.max() - values.min() + 1e-9  # avoid dividing by zero
    return lo + (values - values.min()) / span * (hi - lo)


def temp_cmap(t):
    """Map one temperature (deg C) to an RGBA color."""
    lo, hi = TEMP_RANGE
    return _TEMP_CMAP(np.clip((t - lo) / (hi - lo), 0, 1))
