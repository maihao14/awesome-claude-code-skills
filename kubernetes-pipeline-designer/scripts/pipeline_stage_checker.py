#!/usr/bin/env python3
"""
Simple pipeline stage checker.

Usage:
  python pipeline_stage_checker.py path\to\pipeline.yaml --required build,test,scan,deploy,verify
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check pipeline stage names in a YAML file.")
    parser.add_argument("path", help="Pipeline YAML file path")
    parser.add_argument(
        "--required",
        default="build,test,scan,deploy,verify",
        help="Comma-separated list of required stage keywords",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    path = Path(args.path)
    if not path.exists():
        print(f"File not found: {path}")
        sys.exit(2)

    content = path.read_text(encoding="utf-8", errors="ignore").lower()
    required = [s.strip().lower() for s in args.required.split(",") if s.strip()]
    missing = [s for s in required if s not in content]

    if missing:
        print("Missing stages:")
        for stage in missing:
            print(f"- {stage}")
        sys.exit(1)

    print("All required stages found.")


if __name__ == "__main__":
    main()
