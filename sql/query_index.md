# SQL Query Index

| File | Purpose | Depends On |
|---|---|---|
| `01_cohort_assignment.sql` | Builds `customer_cohort` — assigns each customer to their first-purchase month | `olist_orders_dataset`, `olist_customers_dataset` |
| `02_cohort_retention_matrix.sql` | Builds `cohort_activity` and the final `cohort_retention_matrix` (matches `Insights.csv` schema: cohort_month, month_number, total_customers, retention_pct) | `01_cohort_assignment.sql` |
| `03_kpi_queries.sql` | Standalone KPI queries: repeat purchase rate, median time-to-second-purchase, month-1 retention by cohort, cohort acquisition volume | `01`, `02` |

## Run order
1. `01_cohort_assignment.sql`
2. `02_cohort_retention_matrix.sql`
3. `03_kpi_queries.sql`

## Output validation
`cohort_retention_matrix` should reproduce the same shape as the uploaded `Insights.csv` (23 cohorts, Sep 2016-Aug 2018, ~95,560 customers at month_number=0).

---
*Prepared by Mohammad Ammar — Apex AnalyticX*
