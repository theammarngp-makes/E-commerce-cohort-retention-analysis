# Cohort Retention Analysis
## Executive Report

<table class="meta-table">
<tr><td class="meta-label">Prepared for</td><td>CEO, Founder, Board, Head of Marketing, Finance</td></tr>
<tr><td class="meta-label">Prepared by</td><td>Mohammad Ammar — Apex AnalyticX</td></tr>
<tr><td class="meta-label">Engagement</td><td>E-Commerce Customer Intelligence Series — Project 3 of 4</td></tr>
<tr><td class="meta-label">Date</td><td>July 2026</td></tr>
</table>

---

## 1. Headline Finding

Across **23 monthly acquisition cohorts** (~95,560 customers, September 2016 – August 2018), average **month-1 retention is just 0.33%** — and no cohort ever exceeds **0.65% retention** in any single post-acquisition month, at any point in its lifecycle.

This is not a "retention decline" in the conventional sense — where a healthy share of customers stay engaged and a tail gradually churns. It is a **near-total absence of repeat purchasing** across the entire customer base. The business is currently operating almost exclusively as a new-customer-acquisition engine.

---

## 2. Business Context & Objective

Marketplace economics depend on the relationship between customer acquisition cost (CAC) and customer lifetime value (CLTV). When repeat purchase behavior is healthy, CAC can be amortized across multiple orders — making acquisition spend increasingly efficient over time. When it isn't, every dollar of acquisition spend must be recovered entirely within a customer's first transaction.

This engagement was commissioned to answer six specific business questions:

1. What percentage of customers make a second purchase, and within what time frame?
2. How does retention differ across monthly acquisition cohorts?
3. Is retention improving, worsening, or flat over time?
4. Which customer segments retain best?
5. At what point in the customer lifecycle does the biggest drop-off occur?
6. What would a realistic retention improvement mean in revenue terms?

---

## 3. Methodology (Summary)

Each customer was assigned to a **cohort month** based on the calendar month of their first valid (delivered, non-canceled) purchase. Every subsequent order was mapped to a **months-since-cohort** value, producing a customer-month activity table. This was aggregated into a cohort × month retention matrix, converting raw counts into retention percentages relative to each cohort's starting size — the standard cohort-analysis methodology used across subscription and e-commerce retention modeling.

**Pipeline:** SQL (cohort assignment, retention matrix, KPI extraction) → Python/Pandas (validation, EDA) → visualization (heatmap, retention curve). Full technical detail is documented in `docs/09_Data_Model.md` and `docs/10_Methodology.md`, with query-level detail in `sql/`.

---

## 4. Key Findings

### Finding 1 — Repeat purchasing is structurally rare, not just "low"
Average month-1 retention across mature cohorts (Jan–Jun 2017, i.e., cohorts with enough elapsed time to be fully observed) is **0.33%**. The single best-performing cohort in the entire dataset — August 2017 — still only reached **0.65%** month-1 retention. The worst — July 2018 — reached just **0.099%**. Every cohort, without exception, falls in this narrow, extremely low band.

### Finding 2 — Retention did not improve as the business scaled
Cohort size (i.e., new-customer acquisition volume) grew roughly **8x** from the earliest cohorts (762 customers, January 2017) to typical 2018 cohorts (6,000–7,000+ customers). Year-over-year, acquisition grew from **43,468 customers in 2017 to 51,792 in 2018**. Despite this substantial scale-up, month-1 retention showed no upward trend — later 2018 cohorts perform similarly to, or slightly worse than, the best 2017 cohorts. **Scale alone will not resolve this — it requires a deliberate intervention.**

### Finding 3 — What repeat purchasing exists is front-loaded
Across mature cohorts, retention is (relatively) highest in months 1–2 (0.33%–0.36%), declines through months 3–8 (0.20%–0.32%), and flattens near a floor of ~0.15% by month 13 and beyond. This defines a **narrow, early intervention window** — any re-engagement effort loses effectiveness the longer it waits past the first purchase.

---

## 5. Supporting Visuals

**Cohort Retention Heatmap**

![Cohort Retention Heatmap](img/cohort_heatmap.png)
<p class="caption">Visually confirms Finding 1 — the matrix is near-uniformly dark/near-zero outside the month-0 column across all 23 cohorts.</p>

**Retention Curve**

![Retention Curve](img/retention_curve.png)
<p class="caption">Shows the front-loaded decay pattern described in Finding 3 across the observed 0–19 month window.</p>

**Cohort Size vs. Retention**

![Cohort Size vs Retention](img/cohort_size_trend.png)
<p class="caption">Shows acquisition volume climbing steadily while the retention rate line stays flat — the visual counterpoint to Finding 2.</p>

---

## 6. Business Impact

With retention this low, **customer lifetime value is effectively capped at a single order for the overwhelming majority of customers.** Acquisition spend cannot be amortized over future purchases, which means:

- CAC recovery is a first-order-margin problem today, not a lifetime-value problem
- Reported growth (order volume, GMV) is not evidence of a healthier customer base — it reflects acquisition spend, not loyalty
- The business carries structural exposure to any future increase in acquisition cost (e.g., rising ad costs, increased competition for the same customer pool), since there is no repeat-purchase base to cushion it

**The opportunity side of this is proportionally large.** Because the baseline is so low, even a conservative improvement compounds meaningfully: lifting month-1 retention from 0.33% to 1.5–2% would **multiply the repeat-buyer base 4–6x**, generated entirely from customers already paid for — at a fraction of the marginal cost of acquiring new ones. We have not modeled a specific revenue figure here, as that requires average order value and margin data outside this engagement's scope (see Section 8); the relative-lift framing above is directly supported by the data.

---

## 7. Strategic Recommendations

<table class="custom-cols">
<colgroup>
<col style="width:5%"><col style="width:27%"><col style="width:34%"><col style="width:34%">
</colgroup>
<tr><th>#</th><th>Recommendation</th><th>Rationale</th><th>Expected Impact</th></tr>
<tr>
<td>1</td>
<td><strong>Launch a first-60-day re-engagement trigger</strong> — automated email/discount campaign targeting first-time buyers day 15–45 post-purchase</td>
<td>Findings 1 &amp; 3: retention is both extremely low overall and concentrated in the first 1–2 months; this is the highest-leverage window before customers disengage entirely</td>
<td>4–6x increase in repeat-buyer base from a conservative 0.33%→1.5–2% lift</td>
</tr>
<tr>
<td>2</td>
<td><strong>Investigate root cause before scaling acquisition further</strong> — structured research into delivery experience, seller quality, and marketplace UX</td>
<td>Finding 2: retention did not self-correct with 8x acquisition growth, so the fix is a specific friction point, not "more scale"</td>
<td>Identifying even one major friction point could shift the retention curve materially, not incrementally</td>
</tr>
<tr>
<td>3</td>
<td><strong>Track month-1 / month-3 retention as a standing executive KPI</strong> — added to the core dashboard, cohort by cohort</td>
<td>Finding 2: this problem was invisible under topline GMV/order-volume reporting for the full two-year window observed</td>
<td>Fast feedback loop — a successful intervention should be visible as a step-change in month-1 retention within 1–2 cohort cycles</td>
</tr>
</table>

---

## 8. Limitations & Risks

- **Static, historical dataset.** No ability to run live A/B tests against these findings directly; recommendations should be piloted and measured going forward.
- **Customer identity risk.** `customer_unique_id` may undercount true repeat behavior if customers used multiple accounts or emails — this would mean true retention is understated, though unlikely to explain a gap this large.
- **No marketing/campaign data available.** We cannot yet distinguish "customers weren't asked to return" from "customers were asked and declined" — this is a key input for Recommendation 2.
- **Recent cohorts are immature.** The most recent months in the dataset have not had enough elapsed time to be fully comparable and were excluded from mature-cohort averages.
- **No revenue/margin data in scope.** Financial impact is described directionally (Section 6); a dollarized ROI model requires AOV and margin inputs from Finance.

---

## 9. Conclusion & Next Steps

This is a structural, business-wide finding, not a segment-level anomaly — and it held constant across two full years of substantial growth. The business currently has no meaningful repeat-purchase engine; it has an acquisition engine.

**Immediate next steps:**
1. Pilot the first-60-day re-engagement campaign against the next 2–3 cohorts and measure month-1 retention lift directly
2. Commission the root-cause research workstream (Recommendation 2) in parallel
3. Add retention KPIs to the executive dashboard now, so both of the above are measurable going forward
4. Cross-reference these cohort findings against **Project 4 — Month-over-Month Growth Analysis** to confirm that reported topline growth is fully explained by new-customer acquisition rather than any hidden retention effect

---

<p class="footer-note">Prepared by Mohammad Ammar — Apex AnalyticX — E-Commerce Customer Intelligence Series.<br>Full methodology, KPI definitions, data dictionary, and query-level detail available in <code>docs/</code> and <code>sql/</code>.</p>
