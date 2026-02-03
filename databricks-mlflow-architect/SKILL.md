---
name: databricks-mlflow-architect
description: Design Databricks lakehouse ML pipelines with Unity Catalog medallion layers, Spark ETL, model zoo evaluation, and MLflow tracking/registry. Use for requests to architect, document, or outline notebook-style plans for Databricks ML workflows, experiment tracking, or governance-ready pipelines.
---

# Databricks MLflow Architect

## Overview
- Build medallion pipeline (Bronze, Silver, Gold) in Unity Catalog.
- Use Spark-first ETL and feature engineering.
- Train and compare multiple models with consistent evaluation.
- Log parameters, metrics, artifacts, and models in MLflow.

## Workflow
1. Gather requirements: source tables, SLA, target variable, compliance, and latency.
2. Design Unity Catalog layout: catalog, schemas, table names, ownership.
3. Define Bronze ingestion: source alignment, incremental vs full loads.
4. Define Silver transformations: cleaning, feature engineering, data quality checks.
5. Define Gold outputs: predictions, evaluation tables, monitoring features.
6. Train model zoo: baseline plus candidate models with consistent splits.
7. Evaluate and select: metrics, cross-validation, business KPIs.
8. Log to MLflow: params, metrics, tags, artifacts, and model registry.
9. Deployment and monitoring: retrain triggers, drift checks, rollback plan.

## Output Format
- Provide a Databricks notebook style outline with markdown headings and code blocks.
- Use PySpark for data steps and MLflow for tracking.
- Include table schemas and key partitioning decisions.

## Safety
- Confirm before overwrite, drop, vacuum, or backfill operations.

## Resources
- `scripts/generate_notebook_outline.py`: Generate a starter notebook outline when the user needs a quick scaffold.
- `references/medallion-checklist.md`: Use for governance, naming, and logging checklists.
- `assets/feature-spec-template.md`: Use as a copyable feature specification template.

## Examples

**User**: "Design a Bronze/Silver/Gold pipeline with Spark ETL and MLflow logging for a demand forecast."

**Output**:
- Notebook outline with Unity Catalog layout, Spark transformations, model zoo training loop, and MLflow logging sections.
