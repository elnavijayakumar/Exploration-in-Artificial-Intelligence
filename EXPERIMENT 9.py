# Experiment 9: Data Visualization Using Matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files
# Upload CSV file
uploaded = files.upload()
# Read dataset
df = pd.read_csv("experiment_9_retail_sales.csv")
# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])
# Calculate revenue
df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]
print("----- RETAIL SALES DATASET -----")
print(df.head())
# Total sales analysis
print("\nTotal Units Sold:", df["Units_Sold"].sum())
print("Total Revenue: Rs.",
 df["Revenue"].sum())
# Monthly revenue analysis
monthly_sales = df.groupby(
 df["Date"].dt.to_period("M"))["Revenue"].sum()
print("\n----- MONTHLY REVENUE -----")
print(monthly_sales)
# Category-wise revenue
category_sales = df.groupby(
 "Category")["Revenue"].sum()
print("\n----- CATEGORY-WISE REVENUE -----")
print(category_sales)
# Region-wise revenue
region_sales = df.groupby(
 "Region")["Revenue"].sum()
print("\n----- REGION-WISE REVENUE -----")
print(region_sales)
# Visualization 1: Monthly Revenue Line Chart
plt.figure(figsize=(9, 5))
monthly_sales.index = monthly_sales.index.astype(str)
plt.plot(
 monthly_sales.index,
 monthly_sales.values,
 marker="o",
 linewidth=2,
 label="Monthly Revenue")
plt.title("Monthly Retail Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (Rs.)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
# Visualization 2: Category-wise Bar Chart
plt.figure(figsize=(8, 5))
category_sales.plot(
 kind="bar",
 color="lightgreen",
 edgecolor="black")
plt.title("Category-wise Revenue Comparison")
plt.xlabel("Product Category")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
# Visualization 3: Region-wise Pie Chart
plt.figure(figsize=(7, 7))
plt.pie(
 region_sales,
 labels=region_sales.index,
 autopct="%1.1f%%",
 startangle=90)
plt.title("Region-wise Revenue Distribution")
plt.tight_layout()
plt.show()
# Visualization 4: Units Sold vs Revenue
plt.figure(figsize=(8, 5))
plt.scatter(
 df["Units_Sold"],
 df["Revenue"],
 color="red",
 marker="o")
plt.title("Units Sold vs Revenue")
plt.xlabel("Units Sold")
plt.ylabel("Revenue (Rs.)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
print("\nData Visualization Completed Successfully!")

OUTPUT
----- RETAIL SALES DATASET -----
 Date Product Category Region Units_Sold Unit_Price Revenue
0 2026-01-05 Laptop Electronics North 3 52000 156000
1 2026-01-12 Phone Electronics South 8 18000 144000
2 2026-01-18 Chair Furniture East 6 3500 21000
3 2026-01-24 Desk Furniture West 4 7200 28800
4 2026-02-03 Laptop Electronics East 2 52000 104000
Total Units Sold: 168
Total Revenue: Rs. 2664300
----- MONTHLY REVENUE -----
Date
2026-01 349800
2026-02 344500
2026-03 430700
2026-04 432400
2026-05 565100
2026-06 541800
Freq: M, Name: Revenue, dtype: int64
----- CATEGORY-WISE REVENUE -----
Category
Electronics 2226000
Furniture 438300
Name: Revenue, dtype: int64
----- REGION-WISE REVENUE -----
Region
East 605700
North 687900
South 696800
West 673900
Name: Revenue, dtype: int64
Data Visualization Completed Successfully!
