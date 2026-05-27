import pandas as pd

df = pd.read_csv("data/sales.csv")
print(df)

total_sales = df['amount'].sum()
average_sales = df['amount'].mean()
highest_sales = df['amount'].max()

