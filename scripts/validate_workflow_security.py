#!/usr/bin/env python3
"""Fail closed on mutable remote GitHub Action references."""
from __future__ import annotations
import pathlib
import re
import sys

USES_RE = re.compile(r"^\s*-?\s*uses:\s*([^#\s]+)", re.MULTILINE)
SHA_RE = re.compile(r"^[0-9a-fA-F]{40}$")

def validate_file(path: pathlib.Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    failures: list[str] = []
    for match in USES_RE.finditer(text):
        value = match.group(1).strip().strip("\"'")
        if value.startswith("./") or value.startswith("docker://"):
            continue
        if "@" not in value:
            failures.append(f"{path}: remote action has no immutable ref: {value}")
            continue
        action, ref = value.rsplit("@", 1)
        if not action or not SHA_RE.fullmatch(ref):
            failures.append(f"{path}: remote action is not pinned to a full commit SHA: {value}")
    return failures

def main() -> int:
    root = pathlib.Path(".github/workflows")
    failures: list[str] = []
    for path in sorted([*root.glob("*.yml"), *root.glob("*.yaml")]):
        failures.extend(validate_file(path))
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print("workflow action references are immutable")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
