-- Author: Mohammad Ammar | Apex AnalyticX
-- Project: E-Commerce Customer Cohort Retention Analysis

-- 02_cohort_retention_matrix.sql
-- Builds the cohort x months-since-acquisition retention matrix.
-- Depends on customer_cohort from 01_cohort_assignment.sql

DROP TABLE IF EXISTS cohort_activity;

CREATE TABLE cohort_activity AS
WITH valid_orders AS (
    SELECT
        c.customer_unique_id,
        o.order_purchase_timestamp
    FROM olist_orders_dataset o
    JOIN olist_customers_dataset c
        ON o.customer_id = c.customer_id
    WHERE o.order_status NOT IN ('canceled', 'unavailable')
),
order_month AS (
    SELECT
        customer_unique_id,
        DATE_TRUNC('month', order_purchase_timestamp)::date AS order_month
    FROM valid_orders
    GROUP BY customer_unique_id, DATE_TRUNC('month', order_purchase_timestamp)::date
)
SELECT
    cc.cohort_month,
    om.order_month,
    (EXTRACT(YEAR FROM om.order_month) - EXTRACT(YEAR FROM cc.cohort_month)) * 12
        + (EXTRACT(MONTH FROM om.order_month) - EXTRACT(MONTH FROM cc.cohort_month)) AS month_number,
    om.customer_unique_id
FROM order_month om
JOIN customer_cohort cc
    ON om.customer_unique_id = cc.customer_unique_id;

-- Final retention matrix: cohort_month, month_number, total_customers, retention_pct
-- Matches the schema of Insights.csv
DROP TABLE IF EXISTS cohort_retention_matrix;

CREATE TABLE cohort_retention_matrix AS
WITH cohort_sizes AS (
    SELECT cohort_month, COUNT(DISTINCT customer_unique_id) AS cohort_size
    FROM cohort_activity
    WHERE month_number = 0
    GROUP BY cohort_month
),
activity_counts AS (
    SELECT
        cohort_month,
        month_number,
        COUNT(DISTINCT customer_unique_id) AS total_customers
    FROM cohort_activity
    GROUP BY cohort_month, month_number
)
SELECT
    ac.cohort_month,
    ac.month_number,
    ac.total_customers,
    ROUND(100.0 * ac.total_customers / cs.cohort_size, 5) AS retention_pct
FROM activity_counts ac
JOIN cohort_sizes cs
    ON ac.cohort_month = cs.cohort_month
ORDER BY ac.cohort_month, ac.month_number;

SELECT * FROM cohort_retention_matrix;
