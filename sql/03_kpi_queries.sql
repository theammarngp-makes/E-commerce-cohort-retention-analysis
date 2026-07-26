-- Author: Mohammad Ammar | Apex AnalyticX
-- Project: E-Commerce Customer Cohort Retention Analysis

-- 03_kpi_queries.sql
-- Standalone KPI queries referenced in docs/11_KPI_Definitions.md
-- Depends on customer_cohort (01) and cohort_activity (02)

-- KPI 1: Repeat purchase rate (customers with 2+ distinct order months, all-time)
WITH order_counts AS (
    SELECT customer_unique_id, COUNT(DISTINCT order_month) AS active_months
    FROM cohort_activity
    GROUP BY customer_unique_id
)
SELECT
    COUNT(*) FILTER (WHERE active_months >= 2) AS repeat_customers,
    COUNT(*) AS total_customers,
    ROUND(100.0 * COUNT(*) FILTER (WHERE active_months >= 2) / COUNT(*), 4) AS repeat_purchase_rate_pct
FROM order_counts;

-- KPI 2: Median time (days) between first and second order, for customers with a repeat purchase
WITH valid_orders AS (
    SELECT c.customer_unique_id, o.order_purchase_timestamp
    FROM olist_orders_dataset o
    JOIN olist_customers_dataset c ON o.customer_id = c.customer_id
    WHERE o.order_status NOT IN ('canceled', 'unavailable')
),
ranked AS (
    SELECT
        customer_unique_id,
        order_purchase_timestamp,
        ROW_NUMBER() OVER (PARTITION BY customer_unique_id ORDER BY order_purchase_timestamp) AS rn
    FROM valid_orders
),
first_second AS (
    SELECT
        f.customer_unique_id,
        s.order_purchase_timestamp - f.order_purchase_timestamp AS gap
    FROM ranked f
    JOIN ranked s
        ON f.customer_unique_id = s.customer_unique_id
        AND f.rn = 1 AND s.rn = 2
)
SELECT
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY EXTRACT(EPOCH FROM gap) / 86400.0) AS median_days_to_second_purchase
FROM first_second;

-- KPI 3: Month-1 retention by cohort (quick-reference version of the full matrix)
SELECT cohort_month, retention_pct AS month_1_retention_pct
FROM cohort_retention_matrix
WHERE month_number = 1
ORDER BY cohort_month;

-- KPI 4: Cohort acquisition volume trend (for cross-reference with MoM Growth Analysis)
SELECT cohort_month, total_customers AS cohort_size
FROM cohort_retention_matrix
WHERE month_number = 0
ORDER BY cohort_month;
