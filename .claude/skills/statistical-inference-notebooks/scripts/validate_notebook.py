#!/usr/bin/env python3
"""
Notebook Validation Script for Statistical Inference Architecture

Validates Jupyter notebooks against the "concisely rigorous" architecture:
1. No abbreviations in markdown cells
2. Motivation paragraphs present for major concepts
3. Code cells follow 2-line discipline (max 2 lines, except plotting)
4. Translation comments present for formula-implementing cells
5. Translation comments follow pattern: # [LaTeX]: [Plain English] ([Concept])

Usage:
    python validate_notebook.py path/to/notebook.ipynb
    python validate_notebook.py path/to/notebook.ipynb --fix-suggestions
"""

import json
import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple

# Common abbreviations to flag
ABBREVIATIONS = {
    'RV': 'Random Variable',
    'PMF': 'Probability Mass Function',
    'PDF': 'Probability Density Function',
    'CDF': 'Cumulative Distribution Function',
    'SE': 'Standard Error',
    'SD': 'Standard Deviation',
    'MSE': 'Mean Squared Error',
    'MVUE': 'Minimum Variance Unbiased Estimator',
    'CRLB': 'Cramér-Rao Lower Bound',
    'MLE': 'Maximum Likelihood Estimator',
    'LLN': 'Law of Large Numbers',
    'CLT': 'Central Limit Theorem',
    'IID': 'Independent and Identically Distributed',
    'WLLN': 'Weak Law of Large Numbers',
    'SLLN': 'Strong Law of Large Numbers'
}

class NotebookValidator:
    def __init__(self, notebook_path: str, show_fix_suggestions: bool = False):
        self.notebook_path = Path(notebook_path)
        self.show_fix_suggestions = show_fix_suggestions
        self.issues = []
        self.warnings = []

        with open(self.notebook_path, 'r', encoding='utf-8') as f:
            self.notebook = json.load(f)

        self.cells = self.notebook.get('cells', [])

    def validate(self) -> bool:
        """Run all validation checks. Returns True if all checks pass."""
        print(f"\n{'='*70}")
        print(f"Validating: {self.notebook_path.name}")
        print(f"{'='*70}\n")

        self.check_abbreviations()
        self.check_motivations()
        self.check_code_cell_discipline()
        self.check_translation_comments()

        # Print results
        self.print_results()

        return len(self.issues) == 0

    def check_abbreviations(self):
        """Check for common abbreviations in markdown cells."""
        print("Checking for abbreviations...")

        for idx, cell in enumerate(self.cells):
            if cell.get('cell_type') == 'markdown':
                source = ''.join(cell.get('source', []))

                for abbr, full in ABBREVIATIONS.items():
                    # Look for abbreviation not in code blocks or LaTeX
                    pattern = r'(?<!`)\b' + abbr + r'\b(?!`)'
                    if re.search(pattern, source):
                        self.issues.append(
                            f"Cell {idx}: Found abbreviation '{abbr}' "
                            f"(should be '{full}')"
                        )

    def check_motivations(self):
        """Check that major sections have motivation paragraphs."""
        print("Checking for motivation paragraphs...")

        for idx, cell in enumerate(self.cells):
            if cell.get('cell_type') == 'markdown':
                source = ''.join(cell.get('source', []))

                # Check if this is a major section (## heading)
                if re.match(r'^##\s+\d+\.\d+\s+', source):
                    # Check if "Motivation:" appears in this cell or next markdown cell
                    has_motivation = 'Motivation:' in source or '**Motivation:**' in source

                    if not has_motivation:
                        # Check next markdown cell
                        for next_idx in range(idx + 1, min(idx + 3, len(self.cells))):
                            next_cell = self.cells[next_idx]
                            if next_cell.get('cell_type') == 'markdown':
                                next_source = ''.join(next_cell.get('source', []))
                                if 'Motivation:' in next_source or '**Motivation:**' in next_source:
                                    has_motivation = True
                                    break

                    if not has_motivation:
                        section_title = source.split('\n')[0].strip()
                        self.warnings.append(
                            f"Cell {idx}: Section '{section_title}' may be missing "
                            f"a motivation paragraph"
                        )

    def check_code_cell_discipline(self):
        """Check that code cells follow 2-line discipline (except plotting)."""
        print("Checking code cell line discipline...")

        for idx, cell in enumerate(self.cells):
            if cell.get('cell_type') == 'code':
                source = ''.join(cell.get('source', []))

                # Skip empty cells and comment-only cells
                code_lines = [line for line in source.split('\n')
                             if line.strip() and not line.strip().startswith('#')]

                # Check if this is a plotting cell
                is_plotting = any(keyword in source.lower()
                                 for keyword in ['plt.', 'plot', 'scatter', 'hist',
                                                'xlabel', 'ylabel', 'title', 'legend'])

                if not is_plotting and len(code_lines) > 2:
                    self.issues.append(
                        f"Cell {idx}: Code cell has {len(code_lines)} lines "
                        f"(should be ≤2 lines)"
                    )
                    if self.show_fix_suggestions:
                        self.issues.append(
                            f"  → Suggestion: Split this cell into multiple cells, "
                            f"each doing one conceptual operation"
                        )

    def check_translation_comments(self):
        """Check that formula-implementing cells have translation comments."""
        print("Checking for translation comments...")

        # Find code cells that likely implement formulas
        for idx, cell in enumerate(self.cells):
            if cell.get('cell_type') == 'code':
                source = ''.join(cell.get('source', []))

                # Skip empty cells and plotting cells
                if not source.strip():
                    continue

                is_plotting = 'plt.' in source or 'plot' in source.lower()
                if is_plotting:
                    continue

                # Check if cell has statistical operations that should have translation
                has_stats_operation = any(keyword in source for keyword in [
                    '.mean()', '.var()', '.std()', 'np.mean', 'np.var', 'np.std',
                    'stats.', 'rvs(', 'sem(', 'ttest', 'interval', 'fisher_information',
                    'bias', 'mse', 'estimates', 'sample_mean', 'standard_error'
                ])

                if has_stats_operation:
                    # Check if first line is a translation comment
                    first_line = source.split('\n')[0].strip()

                    if not first_line.startswith('#'):
                        self.warnings.append(
                            f"Cell {idx}: Statistical operation without translation comment"
                        )
                        if self.show_fix_suggestions:
                            self.warnings.append(
                                f"  → Suggestion: Add comment like "
                                f"'# [Formula]: [Plain English] ([Concept])'"
                            )
                    else:
                        # Check if comment follows pattern (has colon)
                        if ':' not in first_line:
                            self.warnings.append(
                                f"Cell {idx}: Translation comment may not follow pattern"
                            )
                            if self.show_fix_suggestions:
                                self.warnings.append(
                                    f"  → Expected pattern: '# [LaTeX]: [Explanation] ([Concept])'"
                                )

    def print_results(self):
        """Print validation results."""
        print(f"\n{'='*70}")
        print("VALIDATION RESULTS")
        print(f"{'='*70}\n")

        if self.issues:
            print(f"❌ ISSUES FOUND ({len(self.issues)}):\n")
            for issue in self.issues:
                print(f"  {issue}")
        else:
            print("✅ No critical issues found!")

        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):\n")
            for warning in self.warnings:
                print(f"  {warning}")

        print(f"\n{'='*70}")

        if not self.issues and not self.warnings:
            print("✅ Notebook passes all validation checks!")
        elif not self.issues:
            print("✅ Notebook has no critical issues (warnings can be reviewed)")
        else:
            print("❌ Notebook has issues that should be fixed")

        print(f"{'='*70}\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_notebook.py path/to/notebook.ipynb [--fix-suggestions]")
        sys.exit(1)

    notebook_path = sys.argv[1]
    show_fix_suggestions = '--fix-suggestions' in sys.argv

    if not Path(notebook_path).exists():
        print(f"Error: Notebook not found at {notebook_path}")
        sys.exit(1)

    validator = NotebookValidator(notebook_path, show_fix_suggestions)
    passed = validator.validate()

    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
