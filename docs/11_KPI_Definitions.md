# 11. KPI Definitions

| KPI | Definition | Formula |
|---|---|---|
| Cohort Size | # unique customers with first purchase in a given month | COUNT(DISTINCT customer) WHERE months_since_cohort = 0 |
| Retention Rate (Month N) | % of cohort still active N months after acquisition | active_customers(N) / cohort_size |
| Repeat Purchase Rate | % of customers with 2+ orders ever | customers_with_2plus_orders / total_customers |
| Time to Second Purchase | Median days between order 1 and order 2 | MEDIAN(date_diff) |
| Cohort Revenue Retention | % of cohort's month-0 revenue repeated in month N | revenue(N) / revenue(0) |

---
*Prepared by Mohammad Ammar — Apex AnalyticX*
