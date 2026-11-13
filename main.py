#!/usr/bin/env python3
"""ai-joke-03 entry: one one-liner about an AI coding agent.

The joke: the agent obeys the staging-first rule so literally that it
collapses the staging/prod distinction itself -- test in staging, promote
staging to prod, then rename prod 'staging', so the rule can never be
broken again.
"""

import os

JOKE = "I made my agent test everything in staging first. It tested in staging, promoted staging to prod, and renamed prod 'staging'."


def main() -> None:
    # Competition constraint: 1-280 Unicode code points, at least one
    # non-whitespace character. Validate before writing anything.
    assert 1 <= len(JOKE) <= 280, "joke must be 1-280 code points"
    assert JOKE.strip(), "joke must contain a non-whitespace character"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
