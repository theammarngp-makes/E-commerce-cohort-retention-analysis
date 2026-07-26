# Author: Mohammad Ammar | Apex AnalyticX
# Project: E-Commerce Customer Cohort Retention Analysis

"""
02_cohort_construction.py
Build the cohort index and retention matrix from cleaned order data.
Reproduces the same schema as the uploaded Insights.csv:
cohort_month, month_number, total_customers, retention_pct

Run after 01_data_cleaning.py (expects clean_orders.csv in the working dir).
"""

import pandas as pd


def month_diff(later, earlier):
    return (later.dt.year - earlier.dt.year) * 12 + (later.dt.month - earlier.dt.month)


def build_cohort_matrix(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.copy()
    orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"])
    orders["order_month"] = orders["order_purchase_timestamp"].values.astype("datetime64[M]")

    # Cohort month = each customer's first order month
    cohort = (
        orders.groupby("customer_unique_id")["order_month"]
        .min()
        .rename("cohort_month")
        .reset_index()
    )
    orders = orders.merge(cohort, on="customer_unique_id", how="left")

    # De-dupe to one row per customer per active month
    monthly_activity = orders[["customer_unique_id", "cohort_month", "order_month"]].drop_duplicates()

    monthly_activity["month_number"] = (
        (monthly_activity["order_month"].dt.year - monthly_activity["cohort_month"].dt.year) * 12
        + (monthly_activity["order_month"].dt.month - monthly_activity["cohort_month"].dt.month)
    )

    activity_counts = (
        monthly_activity.groupby(["cohort_month", "month_number"])["customer_unique_id"]
        .nunique()
        .rename("total_customers")
        .reset_index()
    )

    cohort_sizes = (
        activity_counts[activity_counts["month_number"] == 0]
        .set_index("cohort_month")["total_customers"]
    )

    activity_counts["retention_pct"] = activity_counts.apply(
        lambda r: round(100 * r["total_customers"] / cohort_sizes[r["cohort_month"]], 5),
        axis=1,
    )

    activity_counts["cohort_month"] = activity_counts["cohort_month"].dt.strftime("%Y-%m")

    return activity_counts.sort_values(["cohort_month", "month_number"]).reset_index(drop=True)


def repeat_purchase_rate(orders: pd.DataFrame) -> float:
    """% of customers active in 2+ distinct calendar months (all-time)."""
    orders = orders.copy()
    orders["order_month"] = pd.to_datetime(orders["order_purchase_timestamp"]).values.astype("datetime64[M]")
    active_months = orders.groupby("customer_unique_id")["order_month"].nunique()
    return round(100 * (active_months >= 2).sum() / len(active_months), 4)


def median_days_to_second_purchase(orders: pd.DataFrame):
    """Median gap (days) between first and second order, for repeat customers only."""
    orders = orders.copy()
    orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"])
    ranked = orders.sort_values(["customer_unique_id", "order_purchase_timestamp"]).copy()
    ranked["rn"] = ranked.groupby("customer_unique_id").cumcount() + 1

    first = ranked[ranked["rn"] == 1].set_index("customer_unique_id")["order_purchase_timestamp"]
    second = ranked[ranked["rn"] == 2].set_index("customer_unique_id")["order_purchase_timestamp"]
    gap_days = (second - first).dt.days.dropna()

    return gap_days.median() if len(gap_days) else None


if __name__ == "__main__":
    orders = pd.read_csv("clean_orders.csv")
    matrix = build_cohort_matrix(orders)
    matrix.to_csv("cohort_retention_matrix.csv", index=False)
    print(matrix.head(20))

    print("\nRepeat purchase rate (%):", repeat_purchase_rate(orders))
    print("Median days to second purchase:", median_days_to_second_purchase(orders))
