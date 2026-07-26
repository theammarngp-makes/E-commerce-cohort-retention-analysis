# Python

## Contents
- `01_data_cleaning.py` - loads raw Olist orders/customers CSVs, filters invalid orders, joins to `customer_unique_id`
- `02_cohort_construction.py` - builds the cohort index and retention matrix (Pandas equivalent of the SQL version); also computes repeat purchase rate and median time-to-second-purchase
- `03_eda_visualization.py` - generates the retention curve, cohort heatmap, and cohort size trend charts (outputs saved to `../images/`)

## Run order
```bash
python 01_data_cleaning.py        # -> clean_orders.csv
python 02_cohort_construction.py  # -> cohort_retention_matrix.csv
python 03_eda_visualization.py    # -> ../images/*.png
```

## Environment
See root `requirements.txt`. Tested with pandas, matplotlib, seaborn.

## Note
`03_eda_visualization.py` has been run against the real cohort data - see `../images/` for output and `../docs/12_Business_Insights.md` for the findings.

---
*Prepared by Mohammad Ammar — Apex AnalyticX*
