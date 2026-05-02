#!/usr/bin/env python3
"""Lint files in patterns/ for the required sections.

Each pattern file (except patterns/README.md) must contain the headings:
  Problem, Mechanism, Required properties, Canonical example,
  When it fits, When it doesn't.

Exits non-zero with a list of offending files and missing sections.
"""

import pathlib
import re
import sys

REQUIRED_HEADINGS = [
    "Problem",
    "Mechanism",
    "Required properties",
    "Canonical example",
    "When it fits",
    "When it doesn't",
]

PATTERNS_DIR = pathlib.Path(__file__).resolve().parent.parent / "patterns"
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)


def headings(text: str) -> set[str]:
    return {m.group(1).strip().rstrip(":") for m in HEADING_RE.finditer(text)}


def main() -> int:
    if not PATTERNS_DIR.is_dir():
        print(f"patterns/ directory not found at {PATTERNS_DIR}", file=sys.stderr)
        return 2

    failures: list[tuple[pathlib.Path, list[str]]] = []
    checked = 0
    for path in sorted(PATTERNS_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        checked += 1
        present = headings(path.read_text(encoding="utf-8"))
        missing = [h for h in REQUIRED_HEADINGS if h not in present]
        if missing:
            failures.append((path, missing))

    if failures:
        print("Pattern lint failed:\n")
        for path, missing in failures:
            rel = path.relative_to(PATTERNS_DIR.parent)
            print(f"  {rel}")
            for h in missing:
                print(f"    - missing heading: {h}")
        return 1

    print(f"Pattern lint passed ({checked} file(s) checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
