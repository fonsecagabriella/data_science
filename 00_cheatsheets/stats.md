# Stats

## Types of features
- scale (numerical)
- categorical
- nominal 

## confidence interval for mean
x +/- z * stddev/sqrt(n)

## confidence interval for proportions
p +/- z * sqrt( (p*(1-p)) / n  )


## standardization - Z-score
z = X-u / stddev (or o)

**Standard Error**
SE = stddev / √n,
(you use SE for z-score if population mean is unknown)

: stdev for sample, o for population


## Effect size
- Always report on effect size
- It’s a quantitative measure of the magnitude of the difference or relationship you found.
- Look for formulas on how to report it, differs for test

## Which test to perform
- z-test or t-test
    - if n<30 or o is unknown (almost always), you use t-distribution; you also use df as n-1 to reduce uncertainty
    - if n>30 you can use normal distribution (z-test)

if n>30 you can use normal distribution
- Goodness of fit test: test if data follows a particular distribution
- Two-sample t-test: two indepent groups
- Paired t-test: same group, before and after
- ANOVA: means of > 2 groups
- chi-squared: categorical data

## How to reject null
- p < alpha
- confidence interval has no zero

-> We never accept the null hypothesis, we fail to reject it

