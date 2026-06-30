import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ── 1. CREATE SAMPLE SALES DATA ──────────────────────────────────────────────
np.random.seed(42)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
categories = ["Electronics", "Clothing", "Food", "Furniture", "Sports"]
regions = ["North", "South", "East", "West"]

rows = []
for month in months:
    for category in categories:
        for region in regions:
            sales = np.random.randint(5000, 50000)
            profit = round(sales * np.random.uniform(0.1, 0.4), 2)
            units = np.random.randint(10, 300)
            rows.append([month, category, region, sales, profit, units])

df = pd.DataFrame(rows, columns=["Month", "Category", "Region", "Sales", "Profit", "Units"])

# Save dataset
df.to_csv("sales_data.csv", index=False)

# ── 2. BASIC EXPLORATION ─────────────────────────────────────────────────────
print("=" * 50)
print("       SALES DATA ANALYSIS REPORT")
print("=" * 50)
print(f"\n📦 Dataset Shape : {df.shape[0]} rows × {df.shape[1]} columns")
print(f"\n📋 Columns       : {list(df.columns)}")
print(f"\n🔍 Missing Values:\n{df.isnull().sum()}")
print(f"\n📊 Summary Stats:\n{df[['Sales', 'Profit', 'Units']].describe().round(2)}")

# ── 3. KEY INSIGHTS ──────────────────────────────────────────────────────────
print("\n" + "=" * 50)
print("         KEY BUSINESS INSIGHTS")
print("=" * 50)

total_sales   = df["Sales"].sum()
total_profit  = df["Profit"].sum()
best_category = df.groupby("Category")["Sales"].sum().idxmax()
best_region   = df.groupby("Region")["Sales"].sum().idxmax()
best_month    = df.groupby("Month")["Sales"].sum().idxmax()

print(f"💰 Total Sales        : ₹{total_sales:,.0f}")
print(f"📈 Total Profit       : ₹{total_profit:,.0f}")
print(f"🏆 Best Category      : {best_category}")
print(f"🌍 Best Region        : {best_region}")
print(f"📅 Best Month         : {best_month}")

# ── 4. VISUALIZATIONS ────────────────────────────────────────────────────────
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Sales Data Analysis Dashboard", fontsize=16, fontweight="bold", y=1.01)

# Chart 1 — Sales by Category (Bar)
cat_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
axes[0, 0].bar(cat_sales.index, cat_sales.values, color=sns.color_palette("Set2", len(cat_sales)))
axes[0, 0].set_title("Total Sales by Category")
axes[0, 0].set_xlabel("Category")
axes[0, 0].set_ylabel("Sales (₹)")
axes[0, 0].tick_params(axis="x", rotation=15)

# Chart 2 — Monthly Sales Trend (Line)
month_order = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
month_sales = df.groupby("Month")["Sales"].sum().reindex(month_order)
axes[0, 1].plot(month_sales.index, month_sales.values, marker="o", color="#2196F3", linewidth=2)
axes[0, 1].set_title("Monthly Sales Trend")
axes[0, 1].set_xlabel("Month")
axes[0, 1].set_ylabel("Sales (₹)")
axes[0, 1].tick_params(axis="x", rotation=45)

# Chart 3 — Sales by Region (Pie)
region_sales = df.groupby("Region")["Sales"].sum()
axes[1, 0].pie(region_sales.values, labels=region_sales.index,
               autopct="%1.1f%%", colors=sns.color_palette("pastel"))
axes[1, 0].set_title("Sales Distribution by Region")

# Chart 4 — Profit by Category (Horizontal Bar)
cat_profit = df.groupby("Category")["Profit"].sum().sort_values()
axes[1, 1].barh(cat_profit.index, cat_profit.values, color=sns.color_palette("Set3", len(cat_profit)))
axes[1, 1].set_title("Total Profit by Category")
axes[1, 1].set_xlabel("Profit (₹)")

plt.tight_layout()
plt.savefig("sales_dashboard.png", dpi=150, bbox_inches="tight")
print("\n✅ Dashboard saved as sales_dashboard.png")
print("✅ Dataset saved  as sales_data.csv")
print("\nAnalysis complete! 🎉")
