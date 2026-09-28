"""
Runs every step in order and saves all six images to output/.

Run:
    python src/run_all.py
"""

import subprocess
import sys
from pathlib import Path

SCRIPTS = [
    "step1_the_default.py",
    "step2_strip_defaults.py",
    "step3_choose_intentionally.py",
    "step4_shape_follows_data.py",
    "step5_compose_the_page.py",
    "anatomy_diagram.py",
]

here = Path(__file__).parent

for script in SCRIPTS:
    print(f"\n--- Running {script} ---")
    subprocess.run([sys.executable, str(here / script)], check=True)

print("\nAll done. Check the output/ folder.")
