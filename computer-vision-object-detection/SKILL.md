---
name: computer-vision-object-detection
description: Plan and implement object detection pipelines in computer vision, including dataset design, labeling, augmentation, model selection, training, evaluation, and deployment. Use when asked to design, optimize, or troubleshoot object detection projects.
---

# Computer Vision Object Detection

## Overview
- Define dataset and labeling guidelines.
- Select model architecture and training framework.
- Evaluate with mAP, precision, recall, and error analysis.
- Package inference for deployment on target hardware.

## Workflow
1. Clarify requirements: classes, latency, accuracy, and deployment target.
2. Design dataset: collection sources, labeling rules, and class balance.
3. Define splits and augmentation strategy.
4. Choose models: baseline plus candidate architectures.
5. Train and tune: hyperparameters, batch size, and learning rate.
6. Evaluate: mAP, per-class metrics, confusion analysis.
7. Export and deploy: ONNX, TensorRT, or edge runtime as needed.
8. Monitor and retrain: drift checks and data refresh plan.

## Output Format
- Provide a dataset spec, training plan, evaluation plan, and deployment steps.
- Include example configs or pseudocode for the chosen framework.

## Safety
- Confirm before destructive dataset actions or overwriting model artifacts.

## Resources
- `scripts/generate_eval_report.py`: Generate a standard evaluation report template.
- `references/annotation-guidelines.md`: Use for labeling rules and QA checks.
- `assets/dataset-card-template.md`: Copyable dataset card template for documentation.

## Examples

**User**: "Create an object detection plan for detecting defects on a production line with edge deployment."

**Output**:
- Dataset plan, model candidates, training and evaluation steps, and edge deployment guidance.
