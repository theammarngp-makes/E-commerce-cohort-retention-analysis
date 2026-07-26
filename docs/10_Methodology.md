# 10. Methodology

## Step 1 - Data Cleaning (Python)
- Filter to valid/delivered orders
- Deduplicate customer-order pairs
- Handle missing/invalid timestamps

## Step 2 - Cohort Assignment (SQL/Python)
- Assign each customer to a cohort month based on first purchase
- Build the cohort index table (customer, cohort_month, order_month, months_since_cohort)

## Step 3 - Retention Table Construction
- Pivot into a cohort x month-since-acquisition matrix
- Convert counts to retention percentages relative to cohort size

## Step 4 - Analysis
- Compare retention curves across cohorts
- Identify best/worst performing cohorts and possible drivers (seasonality, category mix, promotions)

## Step 5 - Visualization
- Cohort heatmap (Python/Tableau)
- Retention curve line chart (overlaid cohorts)

## Tools
SQL (cohort queries) -> Python/Pandas (cohort matrix, EDA) -> Tableau (dashboard)

---
*Prepared by Mohammad Ammar — Apex AnalyticX*
