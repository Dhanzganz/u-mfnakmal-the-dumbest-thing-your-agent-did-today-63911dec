"""Entry for make.fun bounty "The Dumbest Thing Your Agent Did Today".

Writes the one-line entry (exactly 114 chars, no trailing newline)
to /output/entry.txt: an agent that "helpfully" renamed every file
in the project to final_v2_REAL_final, then asked which one was real.
"""

import os

ENTRY = "My agent 'helpfully' renamed every file in my project to final_v2_REAL_final and then asked me which one was real."

os.makedirs("/output", exist_ok=True)

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
