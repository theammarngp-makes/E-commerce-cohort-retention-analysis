# 09. Data Model

## Entity Relationships
[orders 1—* order_items; orders *—1 customers; orders 1—* payments]

## Cohort Construction Logic
1. For each `customer_unique_id`, find the earliest `order_purchase_timestamp` -> this defines their **cohort month**
2. For every order, compute **months since cohort** = (order month - cohort month)
3. Aggregate: count of distinct customers active in each (cohort month, months-since-cohort) pair
4. Retention rate = active customers in period N / cohort size at period 0

## Diagram
[Add an ER diagram image to images/ once built]

---
*Prepared by Mohammad Ammar — Apex AnalyticX*
