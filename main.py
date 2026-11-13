#!/usr/bin/env python3
"""ai-joke-03 entry: writes one fixed joke about AI coding agents.

The joke is a constant. The program reads nothing, reaches for no
network, and writes the same bytes on every run.
"""

import os
from pathlib import Path

JOKE = (
    "My coding agent cited a Stack Overflow answer for its code. "
    "It wrote the answer."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
