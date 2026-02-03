# Contributing to Awesome Claude Code Skills

Thanks for contributing. This repo is focused on code and engineering skills for Claude.

## Skill Requirements

All skills must:

1. Solve a real problem based on actual usage.
2. Include clear, step-by-step instructions and examples.
3. Be safe: confirm before destructive operations.
4. Be tested in Claude.ai, Claude Code, or the API when relevant.
5. Be portable across environments when possible.

## Skill Structure

Create a new folder with your skill name (lowercase and hyphenated):

```
skill-name/
  SKILL.md
```

## SKILL.md Template

```markdown
---
name: skill-name
description: One-sentence description of what the skill does and when to use it.
---

# Skill Name

## Overview

Explain what this skill enables in 1-2 sentences.

## Workflow

1. Step 1
2. Step 2
3. Step 3

## Output Format

Describe the expected output format (tables, code blocks, notebook layout, etc.).

## Examples

**User**: "Example prompt"

**Output**:
```
What the skill should produce
```
```

## Adding Your Skill to README

1. Choose the appropriate category:
   - Data Platforms and MLOps
   - DevOps and Platform Engineering
   - Computer Vision
2. Add your skill in alphabetical order within the category:

```markdown
- [Skill Name](./skill-name/) - One-sentence description.
```

## Pull Request Process

1. Fork the repository
2. Create a branch: `git checkout -b add-skill-name`
3. Add your skill folder with SKILL.md
4. Update README.md with your skill in the appropriate category
5. Commit your changes: `git commit -m "Add [Skill Name] skill"`
6. Push to your fork: `git push origin add-skill-name`
7. Open a Pull Request

## Code of Conduct

- Be respectful and constructive
- Credit original sources and inspirations
- Keep skills concise and focused on executable workflows

Thanks for helping build high-quality code skills.
