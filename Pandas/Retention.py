import pandas as pd 
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns

customers = pd.read_csv("/Users/mohammadammar/Desktop/Ecommerce Sales/olist_customers_dataset.csv")
geolocation=pd.read_csv("/Users/mohammadammar/Desktop/Ecommerce Sales/olist_geolocation_dataset.csv")
order_items=pd.read_csv("/Users/mohammadammar/Desktop/Ecommerce Sales/olist_order_items_dataset.csv")
order_payments=pd.read_csv("/Users/mohammadammar/Desktop/Ecommerce Sales/olist_order_payments_dataset.csv")
orders =pd.read_csv("/Users/mohammadammar/Desktop/Ecommerce Sales/olist_orders_dataset.csv")
products =pd.read_csv("/Users/mohammadammar/Desktop/Ecommerce Sales/olist_products_dataset.csv")


date_cols = [
    "order_purchase_timestamp",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]
df = orders.merge(customers,on="customer_id",how="left")\
      .merge(order_items,on="order_id",how="left")\
      .merge(products,on="product_id",how="left")\
      .merge(order_payments,on="order_id",how="left") 

#Convert date columns to datetime format
df["total"] = df["price"]+df["freight_value"]
for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors="coerce")
  
#  Cohort Retention Analysis Report
df["order_month"] = df["order_purchase_timestamp"].dt.to_period("M")
df["cohort_month"] = df.groupby("customer_unique_id")["order_month"].transform("min")

df["cohort_index"] = (
    (df["order_month"].dt.year - df["cohort_month"].dt.year) * 12 +
    (df["order_month"].dt.month - df["cohort_month"].dt.month)
)
cohort_data = df.groupby(["cohort_month", "cohort_index"])["customer_unique_id"].nunique().reset_index()
cohort_pivot = cohort_data.pivot(
    index="cohort_month",
    columns="cohort_index",
    values="customer_unique_id"
)
retention = cohort_pivot.divide(cohort_pivot.iloc[:,0], axis=0)
print(retention)
plt.figure(figsize=(10,6))
sns.heatmap(retention, annot=True, fmt=".0%", cmap="coolwarm")
plt.title("Cohort Retention Heatmap")
plt.show()
  
