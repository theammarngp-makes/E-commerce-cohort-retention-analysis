-- Author: Mohammad Ammar | Apex AnalyticX
-- Project: E-Commerce Customer Cohort Retention Analysis

-- 01_cohort_assignment.sql
-- Assigns each customer to a cohort month based on their first valid order.
-- Dialect: PostgreSQL (adjust DATE_TRUNC/casts if using MySQL/SQLite)

DROP TABLE IF EXISTS customer_cohort;

CREATE TABLE customer_cohort AS
WITH valid_orders AS (
    SELECT
        o.order_id,
        c.customer_unique_id,
        o.order_purchase_timestamp
    FROM olist_orders_dataset o
    JOIN olist_customers_dataset c
        ON o.customer_id = c.customer_id
    WHERE o.order_status NOT IN ('canceled', 'unavailable')
),
first_purchase AS (
    SELECT
        customer_unique_id,
        MIN(order_purchase_timestamp) AS first_purchase_ts
    FROM valid_orders
    GROUP BY customer_unique_id
)
SELECT
    customer_unique_id,
    DATE_TRUNC('month', first_purchase_ts)::date AS cohort_month
FROM first_purchase;

-- Sanity check: cohort sizes should match month_number = 0 rows in the retention matrix
SELECT cohort_month, COUNT(*) AS cohort_size
FROM customer_cohort
GROUP BY cohort_month
ORDER BY cohort_month;
