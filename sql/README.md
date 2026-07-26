# SQL

## Contents
- `01_cohort_assignment.sql` - assigns each customer to their cohort month (`customer_cohort` table)
- `02_cohort_retention_matrix.sql` - builds `cohort_activity` and the final `cohort_retention_matrix` (matches the schema of the analysis output: cohort_month, month_number, total_customers, retention_pct)
- `03_kpi_queries.sql` - repeat purchase rate, median time-to-second-purchase, month-1 retention by cohort, cohort acquisition volume
- `query_index.md` - run order and dependencies

## Dialect
Written for PostgreSQL. Swap `DATE_TRUNC`/`EXTRACT`/`PERCENTILE_CONT` for MySQL/SQLite equivalents if needed.

## Validated against
Output shape matches the real cohort matrix used in `docs/01_Executive_Summary.md`: 23 cohorts, Sep 2016-Aug 2018, ~95,560 customers, avg month-1 retention ~0.33%.

---
*Prepared by Mohammad Ammar — Apex AnalyticX*
