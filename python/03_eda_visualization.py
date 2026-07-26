# Author: Mohammad Ammar | Apex AnalyticX
# Project: E-Commerce Customer Cohort Retention Analysis

"""
03_eda_visualization.py
Retention curve + cohort heatmap, matching the findings written up in
docs/01_Executive_Summary.md and docs/12_Business_Insights.md.

Run after 02_cohort_construction.py (expects cohort_retention_matrix.csv).
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_matrix(path="cohort_retention_matrix.csv") -> pd.DataFrame:
    return pd.read_csv(path)


def plot_retention_curve(df: pd.DataFrame, mature_cohorts=None, out_path="retention_curve.png"):
    """Average retention curve across a set of 'mature' cohorts (enough elapsed months)."""
    if mature_cohorts is None:
        mature_cohorts = ["2017-01", "2017-02", "2017-03", "2017-04", "2017-05", "2017-06"]

    sub = df[df["cohort_month"].isin(mature_cohorts)]
    curve = sub.groupby("month_number")["retention_pct"].mean()

    plt.figure(figsize=(10, 5))
    curve.plot(marker="o")
    plt.title("Average Retention Curve (Mature Cohorts, Jan-Jun 2017)")
    plt.xlabel("Months Since Acquisition")
    plt.ylabel("Retention Rate (%)")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()
    print(f"Saved {out_path}")


def plot_cohort_heatmap(df: pd.DataFrame, out_path="cohort_heatmap.png"):
    pivot = df.pivot(index="cohort_month", columns="month_number", values="retention_pct")

    plt.figure(figsize=(14, 8))
    sns.heatmap(pivot, cmap="YlOrRd", annot=False, cbar_kws={"label": "Retention %"})
    plt.title("Cohort Retention Heatmap")
    plt.xlabel("Months Since Acquisition")
    plt.ylabel("Acquisition Cohort")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()
    print(f"Saved {out_path}")


def plot_cohort_size_trend(df: pd.DataFrame, out_path="cohort_size_trend.png"):
    sizes = df[df["month_number"] == 0].set_index("cohort_month")["total_customers"]

    plt.figure(figsize=(10, 5))
    sizes.plot(kind="bar", color="steelblue")
    plt.title("New Customers Acquired per Cohort Month")
    plt.xlabel("Cohort Month")
    plt.ylabel("New Customers")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150)
    plt.close()
    print(f"Saved {out_path}")


if __name__ == "__main__":
    df = load_matrix()
    plot_retention_curve(df)
    plot_cohort_heatmap(df)
    plot_cohort_size_trend(df)
