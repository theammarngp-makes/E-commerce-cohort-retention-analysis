# E-Commerce Cohort Retention Analysis

> Part of the Apex AnalyticX consulting-grade analytics portfolio. Project 3 of 4 in the Business Intelligence Suite (following Revenue Analysis and RFM Customer Segmentation).

## Executive Summary
Across 23 monthly cohorts (~95,560 customers, Sep 2016-Aug 2018), month-1 retention averages just 0.33% and never exceeds 0.65% in any cohort. The business has scaled almost entirely through new-customer acquisition, not repeat purchases. Full detail in [docs/01_Executive_Summary.md](docs/01_Executive_Summary.md).

## Business Background
[See docs/02_Business_Background.md]

## Business Problem
Why are customers not returning to purchase again after their first order?

## Objectives
[See docs/04_Business_Objectives.md]

## Stakeholders
[See docs/05_Stakeholders.md]

## Business Questions
[See docs/06_Business_Questions.md]

## Dataset
Olist Brazilian E-Commerce Public Dataset. [See docs/08_Dataset_Overview.md]

## Methodology
Cohort assignment -> retention matrix -> SQL/Python analysis -> Tableau dashboard. [See docs/10_Methodology.md]

## SQL Analytics
See `sql/` — cohort assignment, retention matrix, and KPI queries (repeat purchase rate, median time-to-second-purchase). See `sql/query_index.md` for run order.

## Python Analytics
See `python/` — data cleaning, cohort construction, and EDA/visualization scripts. Generated the heatmap and retention curve in `images/` from the real cohort data.

## Dashboard
See `dashboard/` — Tableau build spec and field dictionary. Static equivalents of the core views are in `images/`.

## Insights
- Repeat purchasing is structurally rare (avg. month-1 retention 0.33%), not just "low"
- Retention did not improve as acquisition volume grew ~8x from 2017 to 2018
- Whatever repeat purchases occur are concentrated in months 1-2, then long-tail low

Full detail in [docs/12_Business_Insights.md](docs/12_Business_Insights.md).

## Recommendations
1. Launch a first-60-day post-purchase re-engagement trigger
2. Investigate root cause (delivery, seller quality, marketplace UX) before scaling acquisition further
3. Track month-1/month-3 retention as a core dashboard KPI going forward

Full detail in [docs/13_Business_Recommendations.md](docs/13_Business_Recommendations.md).

## Business Impact
A conservative lift from 0.33% to 1.5-2% month-1 retention would multiply the repeat-buyer base 4-6x at a fraction of new-customer acquisition cost.

## Repository Structure
```
E-commerce-cohort-retention-analysis/
├── assets/
├── dashboard/
├── docs/
├── images/
├── presentation/
├── python/
├── reports/
├── sql/
├── README.md
├── LICENSE
└── requirements.txt
```

## Deliverables
- Full business documentation (docs/)
- SQL cohort queries
- Python cohort construction + EDA notebooks
- Tableau retention dashboard
- Executive report & presentation

## Future Improvements
- Predictive churn model
- Marketing campaign attribution overlay
- Automated monthly cohort refresh pipeline

## Related Projects
- [Olist Revenue & BI Analysis](https://github.com/theammarngp-makes/olist-sales-analysis)
- [RFM Customer Segmentation](https://github.com/theammarngp-makes/ecommerce-rfm-customer-segmentation)
- Month-over-Month Growth Analysis (next in series)

## Author
**Mohammad Ammar** — Founder, Apex AnalyticX
Data Analyst | Business Intelligence | Analytics Consulting
