# Cognitive Takeaways: Chapter 8 - Non-parametric and Robust Inference

## The Core Question We're Bad At

**We confuse "optimal under ideal conditions" with "good in practice."** We use methods that are theoretically best but catastrophically fail when assumptions are violated.

## What We're Bad At (Without Robustness Thinking)

### 1. Recognizing When Optimality is Fragile
- **Naive belief:** "This method is optimal, so I should use it"
- **Reality:** Optimal under very specific assumptions that may not hold
- **Example:** Sample mean is optimal for normal data, catastrophic with one outlier

### 2. Understanding Breakdown Points
- **Illusion:** "One bad data point won't matter much"
- **Reality:** Single outlier can make sample mean arbitrarily wrong
- **Formula:** Sample mean breakdown point = 1/n (worst possible)

### 3. Trading Efficiency for Robustness
- **Temptation:** "I'll accept 5% efficiency loss" seems like a small cost
- **Reality:** Gaining protection against catastrophic failure for tiny efficiency cost is almost always worth it
- **Example:** Median is 57% less efficient but never breaks down until >50% contamination

### 4. Trusting Parametric Tests Without Checking Assumptions
- **Bad habit:** "n > 30, so t-test is fine by Central Limit Theorem"
- **Problem:** Central Limit Theorem requires many more observations for heavily skewed/heavy-tailed data
- **Safe choice:** Use non-parametric test when uncertain

### 5. Ignoring That Assumptions Are Always Wrong
- **Fantasy:** "I checked normality, assumptions hold"
- **Reality:** No data are exactly normal; question is whether violations matter
- **Robustness:** Methods that work well even when assumptions fail

## What Non-parametric and Robust Methods Give Us

### 1. Validity Without Distributional Assumptions
- **Distribution-free:** Valid for any continuous distribution
- **No asymptotic reliance:** Permutation tests are exact, not approximate
- **Peace of mind:** Know your inference is valid even if distributional assumptions are uncertain

### 2. Protection Against Outliers
- **Breakdown point:** Quantifies worst-case robustness
- **Rank-based methods:** Outliers become just highest ranks, limiting influence
- **Median Absolute Deviation:** Robust scale estimation immune to extreme values

### 3. Guaranteed Validity Under Violations
- **Non-parametric tests:** Remain valid when parametric assumptions fail
- **Sign test:** Requires only continuity
- **Wilcoxon:** Requires symmetry, but not normality
- **Mann-Whitney:** Requires same distribution shape, but not normality

### 4. Practical Compromise Options
- **Trimmed mean:** More efficient than median, more robust than mean
- **20% trim:** Removes 10% from each tail, breakdown point = 0.2
- **Best of both worlds:** Good efficiency under normality, protection against outliers

### 5. Empirical Uncertainty Quantification
- **Bootstrap:** Works for any statistic without theoretical formulas
- **Non-parametric:** Makes minimal assumptions about distribution
- **General-purpose:** Standard Errors, confidence intervals, bias correction

## Core Cognitive Reframes

### From: "This method is optimal"
### To: "This method is optimal under what assumptions? What happens when they fail?"

### From: "One outlier won't matter"
### To: "Sample mean has breakdown point 1/n—one outlier CAN make it arbitrarily wrong"

### From: "t-test is always appropriate for comparing means"
### To: "t-test optimal for normal data; Mann-Whitney safer when uncertain"

### From: "Efficiency is most important"
### To: "Robustness matters more than efficiency when assumptions are uncertain"

### From: "I need exact distributional theory"
### To: "Permutation tests and bootstrap provide valid inference without theory"

## The Meta-Insights

### 1. Robustness versus Efficiency Tradeoff is About Insurance

**Insurance Framing:**
- **Efficiency:** Performance under best-case (normal data, no outliers)
- **Robustness:** Protection against worst-case (contamination, violations)
- **Question:** Pay small efficiency premium for catastrophic failure protection?

**Rational Choice:**
- If 100% confident assumptions hold → Use efficient estimator (sample mean, t-test)
- If 95% confident → Probably still use efficient estimator
- If < 90% confident or catastrophic failure is costly → Use robust estimator (median, Wilcoxon)

**Reality:** We are rarely >90% confident distributional assumptions hold exactly.

**Wisdom:** Default to robust methods unless strong evidence for normality AND low contamination risk.

### 2. Breakdown Point is the Ultimate Robustness Measure

**Definition:** Smallest contamination fraction that can make estimator arbitrarily wrong.

**Why it matters:**
- **Sample mean:** Breakdown point = 1/n (one outlier breaks it)
- **Sample median:** Breakdown point = 0.5 (need >50% contamination to break it)
- **Trimmed mean (20%):** Breakdown point = 0.2

**Cognitive anchor:**
- If your data could have even one serious outlier → Don't use sample mean
- If you can tolerate breakdown at 20% contamination → Trimmed mean
- If you want maximum protection → Median

**Life parallel:** Don't optimize for average case if worst case is catastrophic.

### 3. Ranks Are Natural Robustness

**Why ranks work:**
- Outlier becomes just "highest rank," not arbitrarily large value
- Preserves ordering information while limiting extreme influence
- Makes tests valid without distributional assumptions

**Cognitive insight:** Converting to ranks is like capping the influence of extremes.

**Application beyond statistics:**
- When aggregating opinions, ranks reduce influence of extreme outliers
- When comparing performance, ranks handle scale differences automatically

### 4. Non-parametric ≠ Weaker

**Common misconception:** "Non-parametric tests have less power"

**Reality:**
- **Under normality:** Non-parametric tests are ~95% as powerful as t-test
- **Under violations:** Non-parametric tests are MORE powerful (parametric tests lose power badly)
- **Practical conclusion:** Small efficiency cost under ideal conditions, large gain under violations

**Reframe:** Non-parametric tests are more robust, not weaker. They maintain validity and power across broader conditions.

## Practical Wisdom

1. **Default to robust methods when distributional assumptions uncertain:** Median and Mann-Whitney are safer defaults than mean and t-test unless you have strong evidence for normality.

2. **Trimmed mean offers practical compromise:** 10-20% trimmed mean is efficient under normality but protected against outliers—often best practical choice.

3. **Check breakdown points before choosing estimator:** If your data could have outliers, don't use estimators with breakdown point < contamination risk.

4. **Use bootstrap for complex statistics:** When theoretical Standard Error formulas are unavailable (trimmed mean, correlation, median), bootstrap provides empirical uncertainty quantification.

5. **Median Absolute Deviation for robust scale:** When estimating spread with potential outliers, use Median Absolute Deviation not standard deviation.

6. **Permutation tests when sample size is small:** With n < 30, asymptotic approximations may be inaccurate—permutation tests are exact.

7. **Report both parametric and non-parametric results:** If they agree, conclusions are robust. If they disagree, investigate why (outliers? non-normality?) and choose appropriate method.

---

# ROBUSTNESS + VALIDITY: Statistical Thinking for Uncertain Worlds

## The Core Framework

**ROBUSTNESS:** Performance doesn't degrade catastrophically under violations.
**VALIDITY:** Inference remains correct across broad range of conditions.

**Statistical parallel:** We live in uncertain worlds where assumptions are always wrong. Robust methods maintain validity despite violations.

---

## Principle 1: Insurance Against Worst Case

**Statistical concept:** Breakdown point and robustness

**The bug:** You optimize for average case, ignore worst case.
**Example:** Use sample mean (optimal on average) even though one outlier can destroy it

**The fix:**
- **ASK:** "What's worst case? Can I tolerate that?"
- **DO:** Choose method based on acceptable worst-case, not just average-case performance
- **VALIDATE:** Check if robustness is worth small efficiency cost

**Robustness + Validity:**
- **Efficiency-focused:** "Sample mean is optimal (57% more efficient than median)"
- **Robustness-focused:** "But breakdown point is 1/n—one outlier breaks it"
- **Rational choice:** Accept 57% efficiency loss for breakdown point 0.5 (median)

**Life parallel:** Insurance is "inefficient" (expected loss from premiums > expected payout). But rational because protects against catastrophic loss.

---

## Principle 2: Assumptions Are Always Wrong

**Statistical concept:** Distributional assumptions and non-parametric methods

**The bug:** You act as if assumptions are exactly true.
**Example:** "I checked normality with Shapiro-Wilk, p > 0.05, so data are normal"

**The fix:**
- **ASK:** "How wrong can assumptions be before method fails?"
- **DO:** Use methods that maintain validity under broader conditions
- **VALIDATE:** Choose robust methods when consequences of violations are severe

**Robustness + Validity:**
- **Optimistic:** "Assumptions approximately hold, parametric test is fine"
- **Realistic:** "Assumptions are never exact; how robust is my method to violations?"
- **Safe choice:** Non-parametric test valid regardless of distribution

**Life parallel:** Plans assume perfect conditions. Build in slack for when assumptions fail (they always do).

---

## Principle 3: Optimize for Broad Conditions, Not Narrow Ideal

**Statistical concept:** Non-parametric tests maintain power across distributions

**The bug:** You optimize for one specific scenario.
**Example:** "I'll use method optimal for normal data" (but data may not be normal)

**The fix:**
- **ASK:** "How does this perform across range of plausible scenarios?"
- **DO:** Choose methods that work well broadly, not just optimal narrowly
- **VALIDATE:** Test performance under violations, not just under ideal assumptions

**Robustness + Validity:**
- **Narrow optimization:** "t-test is optimal for normal data"
- **Broad optimization:** "Wilcoxon is 95% as efficient for normal, but much better for heavy tails"
- **Practical choice:** Sacrifice 5% efficiency for much better worst-case performance

**Life parallel:** Over-optimized solutions are fragile. Build in flexibility and robustness.

---

## Principle 4: Validity Trumps Efficiency

**Statistical concept:** Valid inference versus powerful inference

**The bug:** You chase power/efficiency, compromise validity.
**Example:** Use parametric test with small sample and non-normal data for higher power

**The fix:**
- **ASK:** "Is my inference actually valid under real conditions?"
- **DO:** Ensure validity first, then optimize efficiency
- **VALIDATE:** Check assumptions; use distribution-free methods when uncertain

**Robustness + Validity:**
- **Efficiency-chasing:** "Parametric test has higher power"
- **Validity-focused:** "But is p-value actually valid? Or are nominal 5% actually 15% due to violations?"
- **Correct priority:** Valid 5% test is better than invalid "5%" test

**Life parallel:** Accurate but imprecise measurement beats precise but inaccurate measurement. Get the right answer roughly rather than wrong answer precisely.

---

## Principle 5: Protection Through Limiting Influence

**Statistical concept:** Ranks limit influence of extreme values

**The bug:** You let extreme values dominate.
**Example:** One extreme data point makes sample mean far from typical values

**The fix:**
- **ASK:** "Are extreme values being weighted appropriately?"
- **DO:** Use methods that limit influence of extremes (ranks, trimming, robust estimation)
- **VALIDATE:** Check how much individual observations influence results

**Robustness + Validity:**
- **Unprotected:** Sample mean weights all values equally—extreme outlier has huge influence
- **Protected:** Median ranks values—extreme outlier just becomes "highest rank"
- **Compromise:** Trimmed mean removes extremes, averages middle

**Life parallel:** Don't let extreme voices dominate decisions. Use mechanisms that limit influence of outliers while incorporating information from majority.

---

## Principle 6: Empirical Beats Theoretical Under Uncertainty

**Statistical concept:** Bootstrap and permutation tests

**The bug:** You insist on theoretical formulas even when assumptions don't hold.
**Example:** Use normal-based confidence interval formula even though distribution is skewed

**The fix:**
- **ASK:** "Do I trust my distributional assumptions enough to rely on theory?"
- **DO:** Use empirical methods (bootstrap, permutation) that don't require distributional assumptions
- **VALIDATE:** Empirical methods provide valid inference with minimal assumptions

**Robustness + Validity:**
- **Theory-dependent:** "Normal theory gives 95% confidence interval [a, b]" (but assumes normality)
- **Empirical:** "Bootstrap 95% confidence interval [c, d]" (valid for any distribution)
- **When uncertain:** Empirical methods more trustworthy

**Life parallel:** When models are uncertain, trust data over theory. Empirical validation beats theoretical elegance.

---

## Principle 7: Small Efficiency Loss, Large Protection Gain

**Statistical concept:** Asymptotic relative efficiency of robust methods

**The bug:** You overvalue efficiency, undervalue robustness.
**Example:** "Median is only 63.7% as efficient as mean—too inefficient!"

**The fix:**
- **ASK:** "What am I actually giving up? What am I gaining?"
- **DO:** Frame tradeoff correctly: small efficiency loss for large protection
- **VALIDATE:** Calculate: 63.7% efficiency = need 57% more data. But median never breaks down until >50% contamination.

**Robustness + Validity:**
- **Overemphasis on efficiency:** "Median requires 57% more data for same power"
- **Balanced view:** "Median accepts needing 57% more clean data to handle ANY level of contamination up to 50%"
- **Rational tradeoff:** Small cost under ideal conditions, huge benefit under violations

**Life parallel:** Insurance, redundancy, and slack are "inefficient" under perfect conditions but essential for real conditions.

---

## Principle 8: Exact Beats Approximate When Possible

**Statistical concept:** Permutation tests provide exact p-values

**The bug:** You trust asymptotic approximations even with small samples.
**Example:** Use normal approximation with n=15, when it may not be accurate

**The fix:**
- **ASK:** "Is my sample large enough for asymptotic theory to be accurate?"
- **DO:** Use exact methods (permutation tests) when sample size is small
- **VALIDATE:** Permutation tests are exact for any sample size

**Robustness + Validity:**
- **Approximate:** "Large-sample theory says p ≈ 0.04"
- **Exact:** "Permutation test gives exact p = 0.038"
- **Small samples:** Exact methods eliminate uncertainty from approximations

**Life parallel:** When exact answers are feasible, don't settle for approximations. Computational power makes many exact solutions now practical.

---

## Meta-Framework: Living in Uncertain Worlds

**Reality:** Assumptions are always wrong. Data are always contaminated. Distributions are always approximate.

**Question:** Do you optimize for the ideal world you wish existed, or protect against the messy world that actually exists?

**Robust thinking forces realism:**
1. **Acknowledge violations:** Assumptions never exactly hold
2. **Quantify fragility:** How wrong can things be before methods fail?
3. **Build protection:** Choose methods that maintain validity under violations
4. **Accept costs:** Small efficiency loss is insurance premium

**Without robustness:** Methods break catastrophically from small violations.
**With robustness:** Methods degrade gracefully, maintaining validity.

---

## Decision-Making Algorithm with Robustness Thinking

**For any inference procedure:**

1. **Identify assumptions:** What does this method assume?
2. **Assess plausibility:** How likely are assumptions to hold exactly?
3. **Check fragility:** What happens when assumptions are violated?
4. **Evaluate breakdown:** How much contamination before method fails?
5. **Consider alternatives:** What robust alternatives exist?
6. **Accept tradeoffs:** Is small efficiency loss worth large protection gain?
7. **Choose method:** Match method to confidence in assumptions and cost of catastrophic failure

**This is robustness thinking applied to inference.**

---

## The Brutal Truth About Real Data

**You will encounter:**
- Outliers (data entry errors, measurement issues, true extremes)
- Non-normality (skewness, heavy tails, multimodality)
- Violations (assumptions never exactly hold)
- Small samples (asymptotic theory doesn't apply)

**Parametric methods optimized for ideal conditions fail badly on real data.**

**Robust methods sacrifice slight efficiency under ideal conditions for protection under real conditions.**

**The discipline:** Don't worship efficiency. Prioritize validity and robustness. Accept insurance premiums.

---

## Comparison: Mean versus Median

| **Property** | **Sample Mean** | **Sample Median** |
|-------------|----------------|-------------------|
| **Efficiency (normal)** | 100% (optimal) | 63.7% (need 57% more data) |
| **Breakdown point** | 1/n (one outlier breaks it) | 0.5 (need >50% contamination) |
| **Heavy tails** | Very poor | Excellent |
| **Outliers** | Catastrophic | Unaffected |
| **Computation** | O(n) | O(n log n) |
| **Practical choice** | Use only with high confidence in normality and no outliers | Safe default for real data |

**Lesson:** Accept 57% efficiency loss to gain protection against catastrophic failure. Usually worth it.

---

## The Core Insight

**Real world ≠ Ideal world. Methods optimized for ideal world fail in real world.**

Non-parametric and robust methods accept small performance cost under ideal conditions for guaranteed validity and protection under real conditions.

**Wisdom comes from:**
- Recognizing assumptions are always wrong
- Quantifying fragility (breakdown points)
- Prioritizing validity over efficiency
- Building protection against worst case
- Accepting insurance premiums (efficiency loss for robustness gain)

**Bottom line:** Robustness is about living in reality, not fantasy. Ideal-world optimal methods are often real-world disasters. Methods that work well broadly beat methods that work perfectly narrowly.

**Robustness + Validity is the path to inference that actually works.**
