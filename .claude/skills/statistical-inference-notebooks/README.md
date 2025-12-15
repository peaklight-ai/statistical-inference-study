# Statistical Inference Notebooks Skill

A Claude skill for creating and maintaining statistical inference Jupyter notebooks following a "concisely rigorous" pedagogical architecture.

## Purpose

This skill ensures notebooks balance mathematical rigor, conceptual clarity, and practical code execution. It enforces:
- No abbreviations (all terminology spelled out)
- Motivation paragraphs for every concept
- 2-line code cell discipline
- Math-to-code translation comments

## Installation

This is a project-level skill located at:
`.claude/skills/statistical-inference-notebooks/`

It is automatically available when working within this project directory.

## Usage

When working with statistical inference notebooks, Claude will automatically use this skill for:
- Creating new chapter notebooks
- Reviewing existing notebooks for compliance
- Adding translation comments to bridge LaTeX and Python
- Validating notebooks against quality standards

## Validation Script

Test notebooks against architectural requirements:

```bash
python scripts/validate_notebook.py path/to/notebook.ipynb
python scripts/validate_notebook.py path/to/notebook.ipynb --fix-suggestions
```

## Resources

- `SKILL.md` - Complete skill documentation with workflows and examples
- `references/architecture.md` - Full architectural philosophy and design rationale
- `references/translation-guide.md` - 10 examples of math-to-code translation comments
- `scripts/validate_notebook.py` - Automated validation tool

## Testing

Tested on Chapter 1 notebook - successfully identified:
- 3 abbreviations needing replacement
- 44 code cells needing translation comments

## Repository

Source project: https://github.com/peaklight-ai/statistical-inference-study
