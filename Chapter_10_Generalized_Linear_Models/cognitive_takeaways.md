# Cognitive Takeaways: Chapter 10 - Generalized Linear Models

## The Core Extension

**Linear regression is just one special case.** Generalized Linear Models provide unified framework for non-normal responses.

## Key Insights

### 1. Link Functions Transform Constraints
- **Problem:** Probabilities must be in [0,1], counts must be positive
- **Solution:** Link function transforms constrained $\mu$ to unconstrained $\eta$
- **Benefit:** Model relationships linearly while ensuring valid predictions

### 2. Three-Component Structure Unifies Diverse Models
- **Random component:** Exponential family distribution
- **Systematic component:** Linear predictor $\eta = X\beta$
- **Link function:** $g(\mu) = \eta$
- **Result:** Linear regression, logistic regression, Poisson regression all fit same framework

### 3. Coefficients Have Multiplicative Interpretations
- **Logistic regression:** $e^\beta$ is odds ratio
- **Poisson regression:** $e^\beta$ is rate ratio
- **Difference from linear:** Additive effects become multiplicative

### 4. Deviance Generalizes Residual Sum of Squares
- **Linear regression:** Fit measured by residual sum of squares
- **Generalized Linear Models:** Fit measured by deviance
- **Use:** Compare nested models via likelihood ratio tests

### 5. Overdispersion is Common
- **Theory:** Variance determined by mean (Poisson, binomial)
- **Reality:** Real data often have greater variability
- **Solution:** Quasi-likelihood, negative binomial, check deviance/degrees of freedom

### 6. Residual Analysis Still Essential
- **Deviance residuals:** Check for patterns
- **Pearson residuals:** Detect outliers
- **Cook's distance:** Identify influential observations
- **Importance:** Good fit requires more than low deviance

### 7. Maximum Likelihood Estimation Provides Asymptotics
- **Method:** Iteratively Reweighted Least Squares
- **Result:** $\hat{\beta} \sim N(\beta, I^{-1})$ asymptotically
- **Inference:** Wald tests, confidence intervals from asymptotic normality

## EXTENSION + UNIFICATION Framework

### Principle 1: Use Right Distribution for Response Type
**Binary → Binomial, Count → Poisson, Continuous → Normal. Don't force wrong distribution.**

### Principle 2: Link Functions Ensure Valid Predictions
**Transform to make relationships linear while keeping predictions in valid range.**

### Principle 3: Interpret on Natural Scale
**Log-odds and log-rates are hard to interpret. Exponentiate to get odds ratios and rate ratios.**

### Principle 4: Check for Overdispersion
**Theory assumes variance determined by mean. Real data often violate this—check deviance/degrees of freedom.**

### Principle 5: Unified Framework Simplifies Analysis
**Once you understand Generalized Linear Model structure, all specific models (logistic, Poisson, etc.) follow same pattern.**

## Practical Wisdom

1. **Logistic regression for binary:** Never use linear regression for 0/1 data
2. **Poisson regression for counts:** But check for overdispersion
3. **Exponentiate coefficients for interpretation:** Odds ratios and rate ratios are more interpretable
4. **Use likelihood ratio tests for nested models:** Compare deviances
5. **Check residual plots:** Patterns indicate model problems
6. **If overdispersed:** Use quasi-likelihood or alternative distribution (negative binomial)
7. **Report both coefficients and exponentiated values:** $\beta$ for statistical testing, $e^\beta$ for interpretation

## The Meta-Insight

**Linear regression assumptions (normal distribution, identity link) are restrictive.** Most real responses don't fit.

**Generalized Linear Models extend to:** Binary outcomes, counts, proportions, positive continuous data.

**Unified framework means:** Learn once, apply everywhere. Same structure, different distributions and links.

**Tradeoff:** More complexity than simple linear regression, but handles much broader class of problems correctly.

**The paradigm:** Don't force data into linear regression. Use appropriate distribution and link for response type.
