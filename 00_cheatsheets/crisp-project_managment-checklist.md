# A CRISP-DM Checklist

## 1) Business Understanding

- **Deliverable:** one-paragraph problem statement, baseline, target, constraints.
- **Questions:** Who uses it? What happens if it's wrong? What's the budget/latency/privacy constraint? Is ML better than rules?
- **Exit criteria:** target metric and guardrails agreed (e.g., reduce spam by 50% with <1% false positives).

## 2) Data Understanding

- **Deliverable:** data map (sources, labels, time range), quality risks.
- **Questions:** Where do labels come from? Any leakage? Enough volume for the target?
- **Exit criteria:** documented issues + feasibility yes/no; sampling script produces a quick EDA.

## 3) Data Preparation

- **Deliverable:** reproducible pipeline to build X, y (or inputs), with versioned splits.
- **Questions:** How are missing/dirty records handled? How are features/inputs created?
- **Exit criteria:** deterministic train/val/test; data quality report; pipeline runs from raw to features.

## 4) Modeling

- **Deliverable:** baseline and 1–2 contenders, with configs and seeds; error analysis.
- **Questions:** Which model meets constraints (latency, interpretability)? Why this loss/metric?
- **Exit criteria:** candidate meets offline targets and budgets; known failure modes listed.

## 5) Evaluation

- **Deliverable:** decision doc (go/no-go), A/B or canary plan, success metric definition.
- **Questions:** What does "good enough" mean in production? What's the ramp plan?
- **Exit criteria:** approved pilot plan with sample size, duration, and stop conditions.

## 6) Deployment

- **Deliverable:** serving path (API/batch), monitoring (drift, latency, errors), retraining trigger, rollback.
- **Questions:** Who is on call? What alerts fire and when? How do we roll back?
- **Exit criteria:** canary passed; dashboards live; retraining job scheduled; owner assigned.
