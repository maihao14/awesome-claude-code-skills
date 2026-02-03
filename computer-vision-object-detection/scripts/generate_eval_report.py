#!/usr/bin/env python3
"""
Generate a simple evaluation report template for object detection.

Usage:
  python generate_eval_report.py --classes person,car,bike
"""

from __future__ import annotations

import argparse
import textwrap


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a detection evaluation report template.")
    parser.add_argument("--classes", default="", help="Comma-separated class list")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    classes = [c.strip() for c in args.classes.split(",") if c.strip()]
    class_rows = "\n".join([f"| {c} |  |  |  |" for c in classes]) or "| all |  |  |  |"

    report = f"""
# Object Detection Evaluation Report

## Summary
- Dataset split:
- Model version:
- Input size:
- Inference latency:

## Metrics
| Class | AP50 | AP50-95 | Recall |
|---|---|---|---|
{class_rows}

## Error Analysis
- False positives:
- False negatives:
- Confusion pairs:

## Deployment Readiness
- Thresholds:
- Known failure modes:
- Rollback plan:
"""

    print(textwrap.dedent(report).strip())


if __name__ == "__main__":
    main()
