# Cognitive Takeaways: Chapter 7 - Common Hypothesis Tests

## The Core Question We're Bad At

**We apply tests mechanically without checking assumptions or choosing appropriately for the question.**

## What We're Bad At

### 1. Using Wrong Test for the Question
- **Habit:** "I have two groups, use t-test" (Independent? Paired? Normal?)
- **Reality:** Test selection depends on design, data type, and assumptions
- **Missing:** Matching test to specific research question

### 2. Ignoring Assumption Violations
- **Optimism:** "I'll use t-test" (without checking normality)
- **Reality:** Violations can invalidate results
- **Solution:** Check assumptions or use robust alternatives

### 3. Not Considering Non-Parametric Alternatives
- **Default:** Always use parametric tests
- **When violated:** Non-parametric tests more appropriate
- **Tradeoff:** Robust but less powerful

## Test Selection Framework

| **Question** | **Parametric Test** | **Non-Parametric Alternative** |
|-------------|-------------------|------------------------------|
| One mean vs value | One-sample t-test | Wilcoxon signed-rank |
| Two independent means | Two-sample t-test | Mann-Whitney U |
| Paired means | Paired t-test | Wilcoxon signed-rank |
| Proportion vs value | Z-test | Exact binomial |
| Two proportions | Two-proportion Z | Fisher's exact |
| Independence | Chi-squared | Fisher's exact (small n) |

## Core Principles

### 1. Design Determines Test
- Independent groups → two-sample test
- Paired/matched → paired test  
- Pairing increases power (accounts for correlation)

### 2. Assumptions Matter
- Parametric tests: Assume distributional form (normal)
- Valid if assumptions hold OR large n (Central Limit Theorem)
- Check assumptions before testing

### 3. Non-Parametric as Backup
- Use when normality questionable
- Based on ranks, not raw values
- Sacrifice power for robustness

## Practical Wisdom

1. **Check assumptions before choosing test**
2. **Use non-parametric tests when assumptions violated**
3. **Paired designs increase power—use when possible**
4. **Chi-squared requires adequate expected counts (≥5)**
5. **Always consider effect size, not just p-value**
6. **For small samples with non-normality, go non-parametric**

**Bottom line:** Know your toolbox. Match test to question, design, and data characteristics. Check assumptions or pay the price in invalid results.
