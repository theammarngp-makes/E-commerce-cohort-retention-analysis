# Cohort Retention Analysis
## Management Report

<table class="meta-table">
<tr><td class="meta-label">Prepared for</td><td>CRM / Marketing Operations, Category Managers, Analytics Team</td></tr>
<tr><td class="meta-label">Prepared by</td><td>Mohammad Ammar — Apex AnalyticX</td></tr>
<tr><td class="meta-label">Engagement</td><td>E-Commerce Customer Intelligence Series — Project 3 of 4</td></tr>
<tr><td class="meta-label">Date</td><td>July 2026</td></tr>
</table>

---

## 1. Objective

Provide the operational detail needed to design, prioritize, and measure a retention intervention — translating the executive-level findings into specific targeting logic, timing windows, and tracking KPIs that CRM/Marketing Ops can act on directly.

---

## 2. Dataset & Scope

| Item | Detail |
|---|---|
| Source | Olist Brazilian E-Commerce dataset (reused from Revenue Analysis and RFM Segmentation projects) |
| Customers analyzed | ~95,560 unique customers (`customer_unique_id`) |
| Time window | September 2016 – August 2018 |
| Cohorts | 23 monthly acquisition cohorts |
| Order filter | Valid orders only (`order_status` excludes `canceled`, `unavailable`) |
| Cohort definition | Customer's earliest `order_purchase_timestamp` → assigned cohort month |
| Retention metric | `active_customers(month N) / cohort_size(month 0)` |

Full field-level detail is in `docs/data_dictionary.md`; full construction logic is in `docs/09_Data_Model.md`.

---

## 3. Full Retention Pattern

| Metric | Value |
|---|---|
| Average month-1 retention (mature cohorts, Jan–Jun 2017) | **0.33%** |
| Best-performing cohort (month-1) | August 2017 — **0.65%** |
| Worst-performing cohort (month-1) | July 2018 — **0.099%** |
| Retention, months 1–2 (relative peak) | 0.33% – 0.36% |
| Retention, months 3–8 (decline phase) | 0.20% – 0.32% |
| Retention, month 13+ (floor) | ~0.15%, with sporadic single-digit-customer upticks (sample noise, not genuine re-engagement) |

![Cohort Retention Heatmap](img/cohort_heatmap.png)
<p class="caption">Full cohort × month retention matrix — near-zero outside the month-0 column across all 23 cohorts.</p>

**Read:** the strongest — and only meaningfully actionable — retention window is **months 1–2 post-purchase**. By month 3, the opportunity has already started to erode; by month 13, it has flattened at a residual floor that is unlikely to represent recoverable behavior without a fundamentally different intervention (e.g., win-back campaigns rather than standard re-engagement).

---

## 4. Cohort Volume Context

| Period | Customers Acquired |
|---|---|
| 2017 | 43,468 |
| 2018 | 51,792 |

| Cohort Size Reference Point | Value |
|---|---|
| Smallest cohort (Jan 2017) | 762 customers |
| Typical 2018 cohort | 6,000 – 7,000+ customers |
| Approximate growth multiple | ~8x |

![Cohort Size vs Retention](img/cohort_size_trend.png)
<p class="caption">Cohort acquisition volume climbing steadily while retention rate stays flat.</p>

**Operational implication:** acquisition volume scaling did not move the retention needle — this rules out "wait for scale to fix it" as a viable strategy and confirms a targeted, designed intervention is required. It also means the addressable audience for a re-engagement pilot is now large enough (thousands of first-time buyers per month) to run a statistically meaningful test quickly.

---

## 5. Recommended Intervention Design

### 5.1 Targeting Window
**Day 15 – Day 45** post-first-purchase. This sits inside the relative-peak retention window (months 1–2) identified in Section 3, while giving enough lead time post-delivery for a genuine second-purchase consideration moment (as opposed to triggering before the first order has even arrived).

### 5.2 Suggested Campaign Structure
<table class="custom-cols">
<colgroup>
<col style="width:14%"><col style="width:12%"><col style="width:28%"><col style="width:46%">
</colgroup>
<tr><th>Touchpoint</th><th>Timing</th><th>Channel</th><th>Intent</th></tr>
<tr><td>Touch 1</td><td>Day 15</td><td>Email</td><td>Soft nudge — "how was your order," light product recommendation, no discount</td></tr>
<tr><td>Touch 2</td><td>Day 30</td><td>Email + on-site banner if logged in</td><td>Incentive introduced (discount/free shipping threshold)</td></tr>
<tr><td>Touch 3</td><td>Day 45</td><td>Email (final)</td><td>Urgency framing on the incentive, last touch before window closes</td></tr>
</table>

*(Exact incentive structure/economics should be validated against margin data by Finance before launch — out of scope for this analysis.)*

### 5.3 Pilot Design
- **Test group:** all first-time buyers from the next 2–3 cohort months
- **Control group:** matched cohort(s) receiving no intervention, or a randomized holdout within the same cohort month
- **Primary success metric:** month-1 retention rate, test vs. control
- **Minimum viable lift to declare success:** any statistically significant increase above the 0.33% mature-cohort baseline; a lift toward 1.5–2% would represent the 4–6x improvement referenced in the Executive Report

---

## 6. Root-Cause Research Workstream (Parallel Track)

Recommended inputs to prioritize, in order of likely diagnostic value:

1. **Delivery performance data** — late/on-time delivery rates, damage/return rates, by cohort and category
2. **Seller-level consistency** — repeat-purchase rate cut by seller, to isolate whether specific sellers are dragging down the average
3. **Support ticket themes** — qualitative review of post-purchase complaints/contact reasons
4. **Existing CRM/campaign history** — confirm whether any prior re-engagement outreach has ever been sent, and if so, why it didn't move retention

This workstream directly informs whether Recommendation 2 from the Executive Report should focus on logistics, seller quality, product/category mix, or platform UX.

---

## 7. KPIs to Track Going Forward

<table class="custom-cols">
<colgroup>
<col style="width:26%"><col style="width:46%"><col style="width:28%">
</colgroup>
<tr><th>KPI</th><th>Definition</th><th>Query Reference</th></tr>
<tr><td>Month-1 retention rate</td><td>% of cohort returning within 1 month of first purchase</td><td><code>sql/03_kpi_queries.sql</code>, KPI 3</td></tr>
<tr><td>Month-3 retention rate</td><td>% of cohort returning within 3 months</td><td>Extend KPI 3 pattern to <code>month_number = 3</code></td></tr>
<tr><td>Repeat purchase rate (all-time)</td><td>% of customers with 2+ distinct order months, ever</td><td><code>sql/03_kpi_queries.sql</code>, KPI 1</td></tr>
<tr><td>Median time to second purchase</td><td>Median days between order 1 and order 2, for repeat customers</td><td><code>sql/03_kpi_queries.sql</code>, KPI 2</td></tr>
<tr><td>Cohort acquisition volume</td><td>New customers per cohort month, for cross-reference with retention rate</td><td><code>sql/03_kpi_queries.sql</code>, KPI 4</td></tr>
</table>

**Recommendation:** these five KPIs should be added to the standing executive/marketing dashboard as a dedicated "Retention" section, refreshed monthly, cohort by cohort — not buried in a one-time report.

---

## 8. Data Caveats for This Workstream

- `customer_unique_id` may not perfectly capture repeat behavior if the same customer used multiple accounts or emails — treat the 0.33% figure as a reasonable floor estimate, not necessarily an exact one
- No marketing spend or historical campaign data was available in this dataset — the pilot design in Section 5 assumes no prior re-engagement outreach has been tested; confirm this before launch
- Seasonality has not been fully isolated from genuine retention trend in this pass — if the root-cause workstream (Section 6) surfaces strong seasonal patterns, revisit the cohort comparisons with seasonal adjustment

---

## 9. Supporting Technical Artifacts

| Artifact | Location |
|---|---|
| Cohort assignment logic | `sql/01_cohort_assignment.sql` |
| Retention matrix construction | `sql/02_cohort_retention_matrix.sql` |
| KPI queries | `sql/03_kpi_queries.sql` |
| Data cleaning pipeline | `python/01_data_cleaning.py` |
| Cohort construction (Python) | `python/02_cohort_construction.py` |
| EDA / visualization | `python/03_eda_visualization.py` |
| Full KPI definitions | `docs/11_KPI_Definitions.md` |
| Data dictionary | `docs/data_dictionary.md` |

---

<p class="footer-note">Prepared by Mohammad Ammar — Apex AnalyticX — E-Commerce Customer Intelligence Series.<br>This report is intended for operational use by CRM, Marketing, and Analytics teams executing on the Executive Report's recommendations.</p>
