"""Laugh Track: The Crypto Trading Joke Contest.

One line about crypto trading life: the group chat says buy the dip,
the trader obeys, and the dip keeps dipping. Setup, turn, punchline.
"""

import os

ENTRY = "The group chat said buy the dip, so I bought the dip. Then the dip bought a shovel and kept digging."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
entry_path = os.path.join(output_dir, "entry.txt")
with open(entry_path, "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
