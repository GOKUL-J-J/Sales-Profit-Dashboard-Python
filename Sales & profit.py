import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/Gokul/OneDrive/Documents/Sales & Profit.csv')
df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

print(df.head())

df['Order Date'] = pd.to_datetime(df['Order Date'])

total_sales = df['Sales'].sum()
print("Total_Sales:",total_sales)
total_profit = df['Profit'].sum()
print("Total_Profit:",total_profit)
avg_profit = df['Profit'].mean()
print("Avg_Profit:",avg_profit)

df['Month'] = df['Order Date'].dt.month_name()

monthly_sales = df.groupby('Month')['Sales'].sum().sort_values(ascending=False)
print(monthly_sales)

category_profit = df.groupby('Category')['Profit'].sum()
print("High_Profit:",category_profit.idxmax())

loss_products = df[df['Profit'] < 0]
print(loss_products)

region_sales = df.groupby('Region')['Sales'].sum()
print(region_sales)


monthly_sales.plot(kind='line')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()


category_profit.plot(kind='bar')

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.show()


region_sales.plot(kind='pie', autopct='%1.1f%%')

plt.title("Regional Sales")

plt.show()
