---
name: kubernetes-pipeline-designer
description: Design CI/CD pipelines for Kubernetes workloads including container build, test, security scans, Helm or Kustomize packaging, environment promotion, and rollback. Use for requests to plan deployment pipelines, GitOps flows, or cluster release strategies.
---

# Kubernetes Pipeline Designer

## Overview
- Define pipeline stages from code to cluster.
- Specify container build, test, lint, and security scans.
- Choose deployment strategy (rolling, blue/green, canary).
- Support GitOps (Argo CD or Flux) or direct apply flows.

## Inputs to Collect
- Cluster type (EKS, GKE, AKS, or on-prem).
- Container registry and image naming.
- Environments and promotion gates.
- Secrets management and policy constraints.

## Workflow
1. Define repository layout: app source, charts, manifests, and pipeline config.
2. Build and test: unit tests, integration tests, and linting.
3. Security and compliance: SAST, image scanning, policy checks.
4. Package and version: Helm chart or Kustomize overlays.
5. Deploy to dev, staging, and production with approvals.
6. Verify and monitor: health checks, alerts, and rollback criteria.

## Output Format
- Provide pipeline stages as a YAML outline plus a short explanation.
- Include manifest strategy (Helm or Kustomize) and environment promotion rules.
- Include rollback steps and required permissions.

## Safety
- Confirm before cluster-wide changes, namespace deletion, or forced rollbacks.

## Resources
- `scripts/pipeline_stage_checker.py`: Validate that a pipeline file includes required stages.
- `references/gitops-options.md`: Quick notes on GitOps tooling and deployment strategies.
- `assets/pipeline-skeleton.yaml`: Copyable CI/CD skeleton for Kubernetes workflows.

## Examples

**User**: "Design a GitOps pipeline for a multi-tenant Kubernetes cluster using Helm and canary releases."

**Output**:
- Pipeline outline with build, scan, package, deploy, verify, and rollback stages.
