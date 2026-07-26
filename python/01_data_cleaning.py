# Author: Mohammad Ammar | Apex AnalyticX
# Project: E-Commerce Customer Cohort Retention Analysis

"""
01_data_cleaning.py
Load raw Olist tables, filter to valid orders, and prepare the base
orders/customers frame used by the cohort construction step.

Expects raw CSVs (Olist Kaggle export) in a local ./raw_data/ folder:
- olist_orders_dataset.csv
- olist_customers_dataset.csv
"""

import pandas as pd

RAW_DIR = "raw_data"


def load_and_clean():
    orders = pd.read_csv(f"{RAW_DIR}/olist_orders_dataset.csv", parse_dates=["order_purchase_timestamp"])
    customers = pd.read_csv(f"{RAW_DIR}/olist_customers_dataset.csv")

    # Filter to valid orders only
    orders = orders[~orders["order_status"].isin(["canceled", "unavailable"])].copy()

    # Drop rows with missing purchase timestamp (shouldn't be many, but check)
    n_before = len(orders)
    orders = orders.dropna(subset=["order_purchase_timestamp"])
    n_after = len(orders)
    if n_before != n_after:
        print(f"Dropped {n_before - n_after} rows with missing order_purchase_timestamp")

    # Join to get customer_unique_id on every order
    merged = orders.merge(
        customers[["customer_id", "customer_unique_id"]],
        on="customer_id",
        how="left",
    )

    missing_unique_id = merged["customer_unique_id"].isna().sum()
    if missing_unique_id:
        print(f"Warning: {missing_unique_id} orders have no matching customer_unique_id")

    merged = merged.dropna(subset=["customer_unique_id"])

    return merged[["order_id", "customer_unique_id", "order_purchase_timestamp"]]


if __name__ == "__main__":
    df = load_and_clean()
    print(df.shape)
    print(df.head())
    df.to_csv("clean_orders.csv", index=False)
