# Cognitive Takeaways: Chapter 6 - Hypothesis Testing Fundamentals

## The Core Question We're Bad At

**We confuse "no evidence of effect" with "evidence of no effect."** Failing to reject the null hypothesis doesn't prove it's true—just that we lack sufficient evidence against it.

## What We're Bad At

### 1. Misinterpreting P-values
- **Wrong:** "p=0.03 means 3% probability H₀ is true"
- **Right:** "If H₀ were true, we'd see data this extreme 3% of the time"
- **Confusion:** P-value is probability of data given H₀, not probability of H₀ given data

### 2. Confusing Statistical and Practical Significance  
- **Mistake:** "p<0.05 so the effect is important"
- **Reality:** Tiny meaningless effects can be statistically significant with large n
- **Missing:** Always consider effect size alongside p-value

### 3. Treating Fail to Reject as Proof
- **Error:** "p=0.15, therefore H₀ is true"
- **Reality:** Absence of evidence ≠ evidence of absence
- **Missing:** May simply lack power to detect effect

### 4. Ignoring Type II Errors
- **Focus:** Obsess about Type I error (α=0.05)
- **Neglect:** Forget about Type II error (missing real effects)
- **Power:** Need adequate power (typically 80%) to detect effects

## What Hypothesis Testing Gives Us

### 1. Controlled Error Rates
- Type I error (α): False positive rate we choose (typically 5%)
- Power (1-β): Probability of detecting true effects
- Explicit tradeoffs: Can't minimize both errors simultaneously

### 2. Formal Decision Framework
- Start assuming H₀ (burden of proof on alternative)
- Reject only with sufficient evidence (small p-value)
- Binary decision: reject or fail to reject

### 3. P-values: Evidence Quantification
- Continuous measure of evidence against H₀
- Small p-value = data unlikely under H₀ = evidence against it
- Not probability H₀ is true!

## Core Reframes

### From: "p=0.03 means H₀ is probably false"
### To: "If H₀ were true, we'd rarely see data this extreme—evidence against H₀"

### From: "Fail to reject means H₀ is true"
### To: "Insufficient evidence against H₀—could be true or we lack power"

### From: "Statistically significant = important"
### To: "Significant means unlikely under H₀, not necessarily practically meaningful"

## Meta-Insights

### 1. Asymmetry Protects Against False Positives
- Null hypothesis gets benefit of doubt
- Require strong evidence (p<α) to reject
- Reflects that false positives often costlier than false negatives

### 2. Power Analysis is Planning
- Determine required sample size before collecting data
- Ensure adequate power (typically 80%) to detect meaningful effects  
- Underpowered studies waste resources

### 3. Duality with Confidence Intervals
- Reject H₀: μ=μ₀ ⟺ μ₀ not in confidence interval
- Tests and intervals provide same information
- Intervals often more informative (show all plausible values)

## Practical Wisdom

1. **Report effect sizes, not just p-values**
2. **Plan for adequate power (calculate required n)**
3. **Never say "proved" or "disproved" H₀**
4. **Interpret "fail to reject" correctly (not proof of H₀)**
5. **Consider practical significance alongside statistical**

**Bottom line:** Hypothesis tests make decisions with controlled error rates, but require correct interpretation. P-values measure evidence, not truth.
