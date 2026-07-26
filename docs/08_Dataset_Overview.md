# 08. Dataset Overview

## Source
Olist Brazilian E-Commerce Public Dataset (Kaggle) — reused from the Revenue Analysis and RFM projects.

## Tables Used
| Table | Purpose |
|---|---|
| olist_orders_dataset | Order dates, order status |
| olist_order_items_dataset | Order line-level revenue |
| olist_customers_dataset | Customer/unique customer IDs |
| olist_order_payments_dataset | Payment values (if used for revenue cuts) |

## Row Counts
[Fill in after loading: total orders, total unique customers]

## Key Fields for Cohort Analysis
- `customer_unique_id` — identifies a customer across orders
- `order_purchase_timestamp` — used to derive cohort month and activity month
- `order_status` — filter to delivered/valid orders only

---
*Prepared by Mohammad Ammar — Apex AnalyticX*
