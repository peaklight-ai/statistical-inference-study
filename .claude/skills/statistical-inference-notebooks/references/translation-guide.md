# Math-to-Code Translation Comments: Implementation Guide

## Purpose
Every code cell that implements a mathematical concept needs a leading comment that translates the formula from LaTeX into plain English. This bridges the gap between abstract mathematics and concrete implementation.

## Translation Pattern

```
# [LaTeX Formula]: [Plain English Explanation] ([Concept Name])
[code implementing the formula]
```

## Examples

### 1. Expected Value and Bias

**Mathematical Statement:** $E[\hat{\theta}] = \theta$ (unbiasedness)

**Code Implementation:**
```python
# E[θ̂] = θ: Average of estimates equals true parameter (unbiasedness)
estimates = [population.rvs(30).mean() for _ in range(5000)]

# Compute bias = E[θ̂] - θ
bias = np.mean(estimates) - true_mu
print(f"Bias: {bias:.4f}")
```

### 2. Variance Formula

**Mathematical Statement:** $\text{Var}(\bar{X}) = \frac{\sigma^2}{n}$

**Code Implementation:**
```python
# Var(X̄) = σ²/n: Variance of sample mean decreases with sample size
empirical_variance = np.var(estimates)
theoretical_variance = true_sigma**2 / 30
```

### 3. Standard Error

**Mathematical Statement:** $SE(\bar{X}) = \frac{\sigma}{\sqrt{n}}$

**Code Implementation:**
```python
# SE(X̄) = σ/√n: Standard error measures precision of estimator
sample_se = sample_sd / np.sqrt(len(data))
print(f"Standard Error: {sample_se:.2f}")
```

### 4. Mean Squared Error

**Mathematical Statement:** $MSE(\hat{\theta}) = E[(\hat{\theta} - \theta)^2] = Bias^2 + Var(\hat{\theta})$

**Code Implementation:**
```python
# MSE = E[(θ̂ - θ)²]: Expected squared distance from truth
mse = np.mean((np.array(estimates) - true_mu)**2)

# MSE = Bias² + Var(θ̂): Decomposition into systematic and random error
print(f"MSE ≈ Variance for unbiased: {np.isclose(mse, empirical_variance)}")
```

### 5. Central Limit Theorem

**Mathematical Statement:** $\frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \xrightarrow{d} N(0,1)$

**Code Implementation:**
```python
# (X̄ - μ)/(σ/√n) → N(0,1): Standardized mean converges to standard normal
standardized_means = [np.sqrt(n) * (pop.rvs(n).mean() - mu) / sigma
                      for _ in range(5000)]
```

### 6. Consistency

**Mathematical Statement:** $\hat{\theta}_n \xrightarrow{P} \theta$ as $n \to \infty$

**Code Implementation:**
```python
# θ̂ₙ →ᴾ θ: Estimator converges in probability to true parameter
distributions_by_n = {n: [population.rvs(n).mean() for _ in range(1000)]
                      for n in sample_sizes}
```

### 7. Cramér-Rao Lower Bound

**Mathematical Statement:** $Var(\hat{\theta}) \geq \frac{1}{nI(\theta)}$

**Code Implementation:**
```python
# Var(θ̂) ≥ 1/(nI(θ)): Minimum variance for unbiased estimators (CRLB)
fisher_information = 1 / true_sigma**2
cramer_rao_bound = 1 / (30 * fisher_information)
```

### 8. Confidence Interval

**Mathematical Statement:** $\bar{X} \pm t_{\alpha/2, n-1} \cdot \frac{s}{\sqrt{n}}$

**Code Implementation:**
```python
# CI = X̄ ± t(α/2) × SE: Range that captures μ with specified confidence
standard_error = stats.sem(data)
ci = stats.t.interval(0.95, len(data)-1, loc=mu_hat, scale=standard_error)
```

### 9. Hypothesis Test Statistic

**Mathematical Statement:** $t = \frac{\bar{X} - \mu_0}{s/\sqrt{n}}$

**Code Implementation:**
```python
# t = (X̄ - μ₀)/(s/√n): Standardized distance from null hypothesis value
test_result = stats.ttest_1samp(data, 105)
print(f"Test statistic: {test_result.statistic:.3f}")
```

### 10. Law of Large Numbers

**Mathematical Statement:** $\bar{X}_n \xrightarrow{P} \mu$ as $n \to \infty$

**Code Implementation:**
```python
# X̄ₙ →ᴾ μ: Sample mean converges to population mean as n increases
means_by_size = [population.rvs(n).mean() for n in sample_sizes]
```

## Guidelines for Writing Translation Comments

### DO:
✅ **Start with the mathematical notation** exactly as it appears in the markdown
```python
# E[θ̂] = θ: ...
```

✅ **Use plain English** that anyone with basic statistics knowledge can understand
```python
# E[θ̂] = θ: Average of estimates equals true parameter
```

✅ **Explain what the formula means**, not just translate symbols
```python
# SE(X̄) = σ/√n: Standard error decreases with square root of sample size
```

✅ **Include the concept name** when helpful
```python
# E[θ̂] = θ: Average of estimates equals true parameter (unbiasedness)
```

✅ **Keep it concise** - one line maximum for the translation

### DON'T:
❌ **Don't just restate symbols**
```python
# Calculate E of theta hat minus theta  ← BAD
```

❌ **Don't assume knowledge of what symbols mean**
```python
# Compute CRLB  ← BAD (spell out Cramér-Rao Lower Bound)
```

❌ **Don't use abbreviations**
```python
# SE = SD/sqrt(n)  ← BAD (spell out Standard Error and Standard Deviation)
```

❌ **Don't write multi-line translation comments**
```python
# This computes the expected value  ← BAD (be concise)
# of the estimator which should equal
# the true parameter value
```

## When to Add Translation Comments

### ALWAYS add for:
- Formula implementations (bias, variance, MSE)
- Distributional results (sampling distributions, asymptotic normality)
- Test statistics and confidence intervals
- Convergence demonstrations (LLN, consistency)

### OPTIONAL for:
- Simple setup code (creating populations, samples)
- Pure visualization code (plotting)
- Print statements showing results

## Complete Example: Unbiasedness Section

**Before (no translation comments):**
```python
estimates_mu = [population.rvs(30).mean() for _ in range(5000)]

bias = np.mean(estimates_mu) - true_mu
print(f"Bias: {bias:.4f}")
```

**After (with translation comments):**
```python
# E[θ̂] = θ: Verify sample mean is unbiased by computing average of estimates
estimates_mu = [population.rvs(30).mean() for _ in range(5000)]

# Bias = E[θ̂] - θ: Difference between average estimate and true parameter
bias = np.mean(estimates_mu) - true_mu
print(f"Bias: {bias:.4f} (≈ 0 confirms unbiasedness)")
```

## Implementation Checklist

When updating a notebook:
- [ ] Identify all cells implementing mathematical concepts
- [ ] For each cell, find the corresponding LaTeX formula in markdown above
- [ ] Write translation comment following the pattern
- [ ] Ensure comment adds value (explains, doesn't just repeat)
- [ ] Keep comment to one line
- [ ] Use plain English, no jargon or abbreviations
- [ ] Test that a student reading the comment would understand what the code does

## Benefits

1. **Reduces cognitive load** - no need to mentally translate LaTeX to code
2. **Makes formulas concrete** - see exactly how abstract math becomes Python
3. **Aids debugging** - clear what each cell should compute
4. **Improves scannability** - can understand code without reading markdown
5. **Teaches connection** - shows relationship between theory and implementation

## Conclusion

Translation comments are the bridge between mathematical rigor and computational practice. They make our "concisely rigorous" approach complete by ensuring students never lose track of which mathematical concept each code cell implements.
