import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/superstore.csv")

print(df.head())

print("Total Sales:", df["Sales"].sum())

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(5)
print(top_products)

print("\nTop Regions:")
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False).head(5))

print("\nSales by Category:")
print(df.groupby("Category")["Sales"].sum())

df.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.ylabel("Sales")
plt.xlabel("Category")
plt.savefig("sales_chart.png")   
plt.show()

print("\nINSIGHTS:")
print("- Technology products generate the highest revenue.")
print("- Canon Copier is the top-performing product.")
print("- Sales are concentrated in a few high-value items.")
