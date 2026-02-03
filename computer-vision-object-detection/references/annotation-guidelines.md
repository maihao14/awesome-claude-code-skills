# Annotation Guidelines

## Bounding Boxes
- Tight box around visible object pixels.
- If occluded, label only the visible area.
- Do not include large background margins.

## Class Rules
- Use consistent class names and definitions.
- Document edge cases (partially visible, reflections, truncated objects).

## Quality Checks
- Minimum box size thresholds.
- Spot check for label drift or class confusion.
- Review a random sample per batch.

## Ignore Regions
- Mark ambiguous areas as ignore where supported.
- Do not label objects smaller than the minimum size threshold.
