# Dashboard Dictionary

Field/calculation definitions for `cohort_retention_dashboard.twbx`.

## Data Source
`cohort_retention_matrix` (output of `sql/02_cohort_retention_matrix.sql` or `python/02_cohort_construction.py`) - columns: `cohort_month`, `month_number`, `total_customers`, `retention_pct`.

## Views

### 1. Cohort Heatmap
- Rows: `cohort_month`
- Columns: `month_number`
- Color: `retention_pct` (sequential color scale, e.g. YlOrRd; cap at ~1-2% given the observed range so the low-retention pattern is visible rather than washed out)

### 2. Retention Curve
- X-axis: `month_number`
- Y-axis: AVG(`retention_pct`)
- Filter: `cohort_month` IN mature cohort list (Jan-Jun 2017) to avoid immature-cohort bias
- Lines: one per cohort, or a single averaged line (toggle via parameter)

### 3. KPI Summary Cards
| Card | Calculation |
|---|---|
| Overall Repeat Purchase Rate | From `sql/03_kpi_queries.sql` KPI 1 |
| Median Days to 2nd Purchase | From `sql/03_kpi_queries.sql` KPI 2 |
| Avg Month-1 Retention | AVG(`retention_pct`) WHERE `month_number` = 1 |
| Total Customers Acquired | SUM(`total_customers`) WHERE `month_number` = 0 |

### 4. Cohort Size Trend (bar chart)
- X-axis: `cohort_month`
- Y-axis: `total_customers` WHERE `month_number` = 0
- Purpose: shows acquisition growth is not matched by retention improvement (cross-reference with Insight 2)

## Calculated Fields
- `Is Mature Cohort`: boolean flag for cohorts with 12+ months of elapsed data as of the latest data date - use to filter comparisons fairly (immature cohorts haven't had time to show later-month retention)

---
*Prepared by Mohammad Ammar — Apex AnalyticX*
