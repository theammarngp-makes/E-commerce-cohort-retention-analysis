 
 -- Cohort Retention %
 
 WITH first_purchase AS (
    SELECT
        c.customer_unique_id,
        MIN(o.order_purchase_timestamp) AS first_purchase_date
    FROM orders o
    JOIN customers c
        ON o.customer_id = c.customer_id
    WHERE o.order_status != 'canceled'
    GROUP BY c.customer_unique_id
),

cohort_data AS (
    SELECT
        DATE_FORMAT(fp.first_purchase_date, '%Y-%m') AS cohort_month,
        
        TIMESTAMPDIFF(
            MONTH,
            fp.first_purchase_date,
            o.order_purchase_timestamp
        ) AS month_number,
        
        c.customer_unique_id
    FROM orders o
    JOIN customers c
        ON o.customer_id = c.customer_id
    JOIN first_purchase fp
        ON c.customer_unique_id = fp.customer_unique_id
    WHERE o.order_status != 'canceled'
)

SELECT
    cohort_month,
    month_number,
    COUNT(DISTINCT customer_unique_id) AS total_customers,
    COUNT(DISTINCT customer_unique_id) * 100.0 /
    FIRST_VALUE(COUNT(DISTINCT customer_unique_id)) 
    OVER (PARTITION BY cohort_month ORDER BY month_number)
    AS retention_pct

FROM cohort_data
GROUP BY cohort_month, month_number
ORDER BY cohort_month, month_number;
