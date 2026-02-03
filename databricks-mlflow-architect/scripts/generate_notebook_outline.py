#!/usr/bin/env python3
"""
Generate a Databricks notebook outline for a medallion ML pipeline.

Usage:
  python generate_notebook_outline.py --catalog main --bronze bronze --silver silver --gold gold \
    --source-table sales_orders --target monthly_demand --experiment exp_sales
"""

from __future__ import annotations

import argparse
import textwrap


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a medallion notebook outline.")
    parser.add_argument("--catalog", default="main", help="Unity Catalog name")
    parser.add_argument("--bronze", default="bronze", help="Bronze schema name")
    parser.add_argument("--silver", default="silver", help="Silver schema name")
    parser.add_argument("--gold", default="gold", help="Gold schema name")
    parser.add_argument("--source-table", default="source_table", help="Bronze source table name")
    parser.add_argument("--target", default="target", help="Target column name")
    parser.add_argument("--experiment", default="mlflow_experiment", help="MLflow experiment name")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    bronze_table = f"{args.catalog}.{args.bronze}.{args.source_table}"
    silver_table = f"{args.catalog}.{args.silver}.{args.source_table}_features"
    gold_predictions = f"{args.catalog}.{args.gold}.{args.source_table}_predictions"

    outline = f"""
# Notebook: Medallion ML Pipeline

## 0. Setup
- Set catalog: `{args.catalog}`
- Schemas: `{args.bronze}`, `{args.silver}`, `{args.gold}`
- MLflow experiment: `{args.experiment}`

## 1. Bronze Read
```python
bronze_df = spark.table("{bronze_table}")
```

## 2. Silver Transformations
```python
# Clean, standardize, and build features
silver_df = bronze_df  # TODO: add transforms
```

## 3. Write Silver
```python
# Confirm before overwrite
silver_df.write.mode("overwrite").saveAsTable("{silver_table}")
```

## 4. Train Model Zoo
```python
# Baseline + candidate models
```

## 5. MLflow Logging
```python
import mlflow
mlflow.set_experiment("{args.experiment}")
```

## 6. Gold Predictions
```python
# Confirm before overwrite
predictions_df.write.mode("overwrite").saveAsTable("{gold_predictions}")
```

## 7. Monitoring
- Drift checks
- Retrain triggers
"""

    print(textwrap.dedent(outline).strip())


if __name__ == "__main__":
    main()
