# Cognitive Takeaways: Chapter 9 - Computationally Intensive Methods

## The Core Transformation

**When theory is impossible, simulate.** Computational methods replace mathematical derivation with empirical approximation.

## Key Insights

### 1. Simulation Replaces Integration
- **Problem:** Can't compute integrals analytically
- **Solution:** Replace $\int h(x)f(x)dx$ with $\frac{1}{N}\sum h(X_i)$ where $X_i \sim f$
- **Power:** Works for any distribution, any dimension, any function

### 2. Resampling Creates Distributions
- **Bootstrap:** Treat sample as population, resample to approximate sampling distribution
- **Permutation:** Generate exact null distribution by permuting labels
- **Benefit:** No distributional assumptions, works for any statistic

### 3. Accuracy Grows Slowly
- **Monte Carlo Standard Error:** $\propto 1/\sqrt{N}$
- **Implication:** Quadruple simulations to halve error
- **Practical:** 1000-10000 simulations usually sufficient

### 4. Exact Tests Without Asymptotic Theory
- **Permutation tests:** Exact p-values for any sample size
- **No reliance on Central Limit Theorem or normality
- **Benefit:** Valid inference even with small samples

### 5. Bootstrap Provides Universal Uncertainty Quantification
- **Standard Errors:** For any statistic (median, trimmed mean, correlation)
- **Confidence intervals:** Percentile method or bootstrap-t
- **Bias correction:** Empirical bias estimate
- **Power:** Works when theoretical formulas don't exist

### 6. Cross-Validation Prevents Overfitting
- **Problem:** Training performance overestimates test performance
- **Solution:** Hold out data, evaluate on unseen observations
- **Result:** Honest assessment of generalization

### 7. Markov Chain Monte Carlo Enables Complex Sampling
- **Problem:** Can't sample directly from posterior or high-dimensional distribution
- **Solution:** Construct Markov chain that eventually samples from target
- **Application:** Makes Bayesian inference practical for complex models

## SIMULATION + EMPIRICAL Framework

### Principle 1: Computation Beats Derivation
**When analytical solution is intractable, simulate your way to the answer.**

### Principle 2: Empirical Distributions Beat Theoretical Approximations
**Bootstrap distribution from data rather than relying on asymptotic theory.**

### Principle 3: Permutation Provides Exact Inference
**Generate null distribution by exhaustive permutation rather than assuming it.**

### Principle 4: Cross-Validation Reveals True Performance
**Test on held-out data rather than trusting training performance.**

### Principle 5: Accept Computational Cost for Broader Applicability
**Trade computer time for fewer assumptions and wider validity.**

## Practical Wisdom

1. **Use permutation tests for small samples:** Exact p-values without asymptotics
2. **Bootstrap when theory is hard:** Standard Errors for complex statistics
3. **Cross-validate all predictive models:** Never trust training performance
4. **10000 simulations for publication:** 1000 for exploration
5. **Check Markov Chain Monte Carlo convergence:** Multiple chains, trace plots, autocorrelation
6. **Parallelize when possible:** Most methods are embarrassingly parallel
7. **Remember √N law:** Doubling accuracy requires 4x computation

## The Meta-Insight

**Computational power transforms impossible problems into routine analyses.** What required pure mathematics 50 years ago now requires simulation.

**Tradeoff:** Exchange mathematical elegance for practical applicability.

**Result:** Broader class of solvable problems, fewer assumptions required, valid inference in more scenarios.

**The paradigm shift:** From "Can I derive this?" to "Can I simulate this?"
