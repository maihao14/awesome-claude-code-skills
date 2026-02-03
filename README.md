# Awesome Claude Code Skills

![Code Banner](./assets/code_banner.png)

This code skill repository focuses on enterprise‑grade Claude and ChatGPT development skills across data platforms, ML, and DevOps. Each skill is self‑contained in its own folder with a clear `SKILL.md` workflow.

If you build tools, design systems, or automate workflows, you’re in the right place. New contributors are welcome.

## Contents
- [Why this repo](#why-this-repo)
- [How to use](#how-to-use)
- [Skills](#skills)
- [How to contribute](#how-to-contribute)
- [Quality bar](#quality-bar)

## Why this repo
Claude Skills are reusable, task‑focused workflows. This collection helps people:
- Ship faster with proven patterns
- Learn practical approaches across domains
- Share reusable building blocks with the community

## How to use
Use Skills in Claude:
1. Open `Settings` → `Capabilities`
2. Enable `Code execution` and `File creation` (required for Skills)
3. In `Skills`, toggle the skills you want
4. Click `Upload skill` and upload a ZIP file containing your skill folder
5. Start a chat and describe your task; Claude will load relevant skills automatically

Use this repository:
1. Pick a skill folder and open its `SKILL.md`
2. Follow the workflow, then adapt it to your project
3. If something’s missing, propose an improvement or add a new skill

Team and Enterprise owners can provision skills org‑wide in Admin settings; users can still toggle them on or off in their own settings.

## Skills

### Data Platforms and MLOps
- [Databricks MLflow Architect](./databricks-mlflow-architect/) - Design Unity Catalog medallion pipelines with Spark ETL, model zoo evaluation, and MLflow tracking.

### DevOps and Platform Engineering
- [Kubernetes Pipeline Designer](./kubernetes-pipeline-designer/) - Design CI/CD pipelines for Kubernetes with build, scan, deploy, and rollback strategies.

### Computer Vision
- [Computer Vision Object Detection](./computer-vision-object-detection/) - Plan data, training, evaluation, and deployment for object detection models.

## How to contribute
We love collaborations, big or small. You can:
- Add a new skill
- Improve an existing skill
- Fix typos, clarity issues, or broken steps
- Suggest new categories

Quick start:
1. Create a new folder with a clear name
2. Add a `SKILL.md` that explains the workflow end‑to‑end
3. Update this README to list the skill

See `CONTRIBUTING.md` for full guidelines.

## Quality bar
Skills should be:
- Actionable and specific
- Easy to follow and implement
- Clearly scoped to a real task
- Maintained with examples or references when helpful
