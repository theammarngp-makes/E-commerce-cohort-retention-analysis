# Data Dictionary

| Field | Table | Type | Description |
|---|---|---|---|
| customer_unique_id | olist_customers_dataset | string | Unique customer identifier across orders |
| order_id | olist_orders_dataset | string | Unique order identifier |
| order_purchase_timestamp | olist_orders_dataset | datetime | Timestamp of order placement |
| order_status | olist_orders_dataset | string | Order status (delivered, canceled, etc.) |
| cohort_month | derived | date | Month of customer's first purchase |
| order_month | derived | date | Month of a given order |
| months_since_cohort | derived | int | order_month - cohort_month, in months |

---
*Prepared by Mohammad Ammar — Apex AnalyticX*
