---
name: statistical-inference-notebooks
description: Create and maintain statistical inference Jupyter notebooks following a "concisely rigorous" architecture. Use when creating new chapters, reviewing existing notebooks, or applying translation comments that bridge LaTeX formulas to Python code. Ensures no abbreviations, motivational paragraphs for every concept, 2-line code cell discipline, and math-to-code translation comments.
---

# Statistical Inference Notebooks

## Overview

This skill implements a pedagogical framework for creating interactive statistical inference notebooks that balance three goals:
1. **Mathematical Rigor** - Precise definitions and formal notation
2. **Conceptual Clarity** - Deep understanding through motivation
3. **Practical Immediacy** - Learning through code execution

The approach is "concisely rigorous": no fluff, proper mathematical formulation, motivated explanations, and hands-on computational verification.

## When to Use This Skill

Use this skill when:
- **Creating new chapter notebooks** for statistical inference topics
- **Reviewing existing notebooks** to ensure architectural compliance
- **Adding translation comments** to bridge LaTeX formulas and Python code
- **Refactoring notebooks** to eliminate abbreviations and add motivations
- **Validating notebooks** against quality standards

## Core Architecture Principles

### 1. No Abbreviations Rule

**ALWAYS spell out full terminology:**
- ✅ Random Variable (not RV)
- ✅ Probability Mass Function (not PMF)
- ✅ Standard Error (not SE)
- ✅ Mean Squared Error (not MSE)
- ✅ Minimum Variance Unbiased Estimator (not MVUE)
- ✅ Cramér-Rao Lower Bound (not CRLB)

**Why:** Abbreviations create cognitive overhead and confusion. Full terms improve clarity and accessibility.

### 2. Motivation-First Design

**EVERY major concept MUST begin with a motivation paragraph explaining:**
1. What problem does this solve?
2. Why can't we use simpler methods?
3. How does this connect to the broader inference framework?

**Example Structure:**
```markdown
## 2.2 Unbiasedness

**Definition:** An estimator $\hat{\theta}$ is unbiased if $E[\hat{\theta}] = \theta$.

**Motivation:** Unbiasedness means the estimator is correct "on average" across all possible samples. If we could repeat the sampling process infinitely many times, the average of all estimates would equal the true parameter. This property ensures our estimation procedure has no systematic error, though individual estimates will still vary due to sampling variability...

[Code demonstrations follow]
```

### 3. Two-Line Code Cell Discipline

**Maximum 2 lines of Python per code cell.**

**Why:**
- Forces focus on one concept per cell
- Enables cell-by-cell execution in Claude Code
- Prevents cognitive overload
- Makes notebooks scannable

**Example:**
```python
# E[θ̂] = θ: Verify sample mean is unbiased
estimates = [population.rvs(30).mean() for _ in range(5000)]
```

```python
# Bias = E[θ̂] - θ: Difference between average estimate and true parameter
bias = np.mean(estimates) - true_mu
print(f"Bias: {bias:.4f} (≈ 0 confirms unbiasedness)")
```

### 4. Math-to-Code Translation Comments

**EVERY code cell implementing a mathematical concept MUST begin with a translation comment:**

**Pattern:** `# [LaTeX Formula]: [Plain English Explanation] ([Concept Name])`

**Examples:**
```python
# E[θ̂] = θ: Average of estimates equals true parameter (unbiasedness)
estimates = [population.rvs(30).mean() for _ in range(5000)]

# Var(X̄) = σ²/n: Variance of sample mean decreases with sample size
empirical_variance = np.var(estimates)
theoretical_variance = true_sigma**2 / 30

# SE(X̄) = σ/√n: Standard error measures precision of estimator
sample_se = sample_sd / np.sqrt(len(data))

# MSE = E[(θ̂ - θ)²]: Expected squared distance from truth
mse = np.mean((np.array(estimates) - true_mu)**2)

# CI = X̄ ± t(α/2) × SE: Range that captures μ with specified confidence
standard_error = stats.sem(data)
ci = stats.t.interval(0.95, len(data)-1, loc=mu_hat, scale=standard_error)
```

**Guidelines:**
- ✅ Start with mathematical notation exactly as it appears in markdown
- ✅ Use plain English that anyone with basic statistics knowledge can understand
- ✅ Explain what the formula means, not just translate symbols
- ✅ Keep it concise - one line maximum
- ❌ Don't just restate symbols
- ❌ Don't use abbreviations
- ❌ Don't assume knowledge of what symbols mean

See `references/translation-guide.md` for 10 detailed examples with DO/DON'T patterns.

## Notebook Creation Workflow

### Step 1: Chapter Planning

1. Identify the chapter topic and core learning goals
2. Outline major concepts that need coverage
3. Determine the logical progression of concepts

### Step 2: Section Structure

For each major concept, follow this pattern:

```markdown
## [Section Number] [Concept Name]

**Definition:** [Precise mathematical definition with LaTeX]

**Motivation:** [3-5 sentences explaining why this concept exists, what problem it solves, and how it connects to inference goals]

**Mathematical Properties:** [Key formulas and theoretical results]

[Code demonstrations follow]

**Interpretation:** [What did we observe? Does it match theory? What does this tell us?]
```

### Step 3: Code Implementation

1. **Setup Cell:** Define parameters and populations
2. **Simulation Cell:** Generate data/estimates (max 2 lines)
3. **Analysis Cell:** Compute statistics (max 2 lines)
4. **Visualization Cell:** Create plots (can be >2 lines for plotting)

**Each cell MUST have a translation comment** if implementing a mathematical concept.

### Step 4: Validation

Before considering a notebook complete, verify:
- [ ] All technical terms spelled out completely (no abbreviations)
- [ ] Every major concept has a motivation paragraph
- [ ] All code cells are ≤2 lines (except visualization)
- [ ] Every formula-implementing cell has a translation comment
- [ ] Translation comments follow pattern: `# [LaTeX]: [Plain English] ([Concept])`
- [ ] All visualizations have labeled axes and titles
- [ ] Interpretation follows every demonstration
- [ ] Notebook executes top-to-bottom without errors

Use `scripts/validate_notebook.py` to check these requirements automatically.

## Four Architectural Layers

### Layer 1: Conceptual (Motivation-First)
- Never introduce a concept without explaining why it exists
- Answer: What problem? Why not simpler methods? How does it connect?

### Layer 2: Mathematical (Precision Without Pedantry)
- Full terminology to avoid confusion
- LaTeX for all expressions: $E[\hat{\theta}] = \theta$
- Formal definitions precede demonstrations
- Omit proofs unless they provide insight

### Layer 3: Computational (Code-First Verification)
- Trust but verify - every theoretical claim should be computationally demonstrable
- Theory → Code → Interpretation pattern
- Translation comments bridge abstract math and concrete code

### Layer 4: Visualization (Seeing is Understanding)
- Show distributions, not just numbers
- Label axes with full names
- Use color meaningfully
- Title should state what we're demonstrating

See `references/architecture.md` for complete architectural philosophy including cognitive load management, progressive disclosure, and anti-patterns to avoid.

## Common Tasks

### Creating a New Chapter

1. Create directory: `Chapter_N_TopicName/`
2. Create notebook: `chapter_N_topic_name.ipynb`
3. Start with imports and overview
4. For each concept: Motivation → Definition → Code → Interpretation
5. End with summary and key takeaways
6. Validate using checklist above

### Adding Translation Comments to Existing Notebook

1. Read the notebook to identify code cells implementing formulas
2. For each cell, find the corresponding LaTeX formula in markdown above
3. Add translation comment following pattern: `# [LaTeX]: [Plain English] ([Concept])`
4. Ensure comment adds value (explains, doesn't just repeat)
5. Test that a student reading the comment would understand what the code does

**Example Transformation:**

**Before:**
```python
estimates_mu = [population.rvs(30).mean() for _ in range(5000)]
bias = np.mean(estimates_mu) - true_mu
print(f"Bias: {bias:.4f}")
```

**After:**
```python
# E[θ̂] = θ: Verify sample mean is unbiased by computing average of estimates
estimates_mu = [population.rvs(30).mean() for _ in range(5000)]

# Bias = E[θ̂] - θ: Difference between average estimate and true parameter
bias = np.mean(estimates_mu) - true_mu
print(f"Bias: {bias:.4f} (≈ 0 confirms unbiasedness)")
```

### Reviewing an Existing Notebook

Use the validation checklist:
1. Scan markdown cells for abbreviations - flag any found
2. Check each major concept has motivation paragraph
3. Count lines in code cells - flag any >2 lines (except plotting)
4. Check formula-implementing cells have translation comments
5. Verify translation comments follow pattern
6. Check visualizations are labeled and interpreted

## Anti-Patterns to Avoid

### ❌ Mathematical Rigor Without Context
```markdown
## Maximum Likelihood Estimator
**Definition:** $\hat{\theta}_{MLE} = \arg\max_\theta L(\theta; x)$
[Code follows immediately]
```
**Why bad:** No motivation for why we maximize likelihood.

### ✅ Correct Approach
```markdown
## Maximum Likelihood Estimator
**Motivation:** Given observed data, which parameter value makes this data most probable? The maximum likelihood estimator chooses the parameter that maximizes the probability of what we actually observed...

**Definition:** $\hat{\theta}_{MLE} = \arg\max_\theta L(\theta; x)$
```

### ❌ Code Without Theory
```python
# Calculate something
result = np.mean(data)
print(result)
```
**Why bad:** No connection to statistical theory.

### ✅ Correct Approach
```python
# E[X̄] = μ: Sample mean is unbiased estimator of population mean
result = np.mean(data)
print(f"Sample mean: {result:.2f}")
```

### ❌ Abbreviation Soup
"The MLE achieves the CRLB, making it MVUE. The SE equals SD/√n."

### ✅ Correct Approach
"The Maximum Likelihood Estimator achieves the Cramér-Rao Lower Bound, making it a Minimum Variance Unbiased Estimator. The Standard Error equals Standard Deviation divided by square root of n."

## Resources

### references/
- **architecture.md**: Complete architectural philosophy with all four layers, cognitive load management, progressive disclosure, quality standards, and design rationale
- **translation-guide.md**: 10 concrete examples of math-to-code translation comments with DO/DON'T guidelines and complete patterns for common formulas

### scripts/
- **validate_notebook.py**: Automated validation script that checks notebooks against architectural requirements (abbreviations, motivations, cell discipline, translation comments)

## Benefits of This Approach

1. **Reduces cognitive load** - No mental translation between LaTeX and code
2. **Makes formulas concrete** - See exactly how abstract math becomes Python
3. **Aids debugging** - Clear what each cell should compute
4. **Improves scannability** - Can understand code without reading all markdown
5. **Teaches connection** - Shows relationship between theory and implementation
6. **Promotes deep understanding** - Motivation-first prevents formula memorization
7. **Enables immediate feedback** - Run code, verify theory, reinforce learning

## Target Learner Profile

**Prerequisites:**
- Calculus (derivatives, integrals)
- Basic probability (distributions, expected value)
- Python fundamentals (lists, loops, functions)

**Goals:**
- Master theoretical foundations of statistical inference
- Develop intuition through computational exploration
- See theory verified in practice

**Learning Style:**
- Prefers understanding over memorization
- Values mathematical precision but needs motivation
- Learns by doing and experimenting
