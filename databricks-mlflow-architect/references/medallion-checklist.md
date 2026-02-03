# Medallion Pipeline Checklist

## Unity Catalog Layout
- Catalog and schema names are explicit and owned by a team.
- Table names indicate source and purpose (example: orders_raw, orders_features).
- Use separate schemas for bronze, silver, and gold.

## Bronze
- Ingestion is source-aligned and append-only when possible.
- Capture ingestion timestamp and source metadata.
- Document late-arriving data handling.

## Silver
- Standardize types, apply deduplication, and add data quality checks.
- Record feature definitions and windowing logic.
- Use partitioning only for large tables with frequent filters.

## Gold
- Store predictions and evaluation summaries in curated tables.
- Keep inference outputs immutable where possible.

## MLflow Logging
- Log parameters, metrics, tags, and at least two artifacts.
- Attach dataset version or snapshot reference in tags.
- Register the selected model with a clear stage transition policy.
