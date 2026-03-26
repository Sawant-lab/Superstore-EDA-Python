import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

## Dataset Load 
df = pd.read_csv('C:/Users/sawan/cleaned_superstore.csv')
print(df.head())

## Dataset Overview
print(df.shape)
print(df.columns)
print(df.describe())

## Sales by Region (business Insight)
sales_region = df.groupby('Region')['Sales'].sum()

sales_region.plot(kind='bar')

plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.show()

## Sales by Category
sales_category = df.groupby('Product Category')['Sales'].sum()

sales_category.plot(kind='bar')

plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Sales")

plt.show()


## Profit Distribution
plt.hist(df['Profit'], bins=30)

plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")

plt.show()

## Sales vs Profit Analysis
plt.scatter(df['Sales'], df['Profit'])

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.show()

## Correlation Heatmap
corr = df.corr(numeric_only=True)

sns.heatmap(corr, annot=True)

plt.title("Correlation Heatmap")

plt.show()




