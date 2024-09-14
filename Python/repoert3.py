import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Connection details
conn_str = (
    r'mssql+pyodbc://m-khorrami/Darina Exam'
    r'?driver=ODBC+Driver+17+for+SQL+Server'
)

# Create an SQLAlchemy engine
engine = create_engine(conn_str)

# Query to fetch data
query = """
SELECT [Product_ID]
      ,[category]
      ,[Sales]
      ,[CumulativePercentage]
  FROM [Darina Exam].[dbo].[Pareto's rule (80/20) for products]
"""

# Fetch the data into a DataFrame
try:
    df = pd.read_sql(query, engine)
    print("Data fetched successfully!")
    print(df)
except Exception as e:
    print(f"An error occurred: {e}")

# Close the connection
engine.dispose()

# Sort by CumulativePercentage
df = df.sort_values('CumulativePercentage')

# Plot: Pareto Analysis (80/20 rule)
plt.figure(figsize=(12, 6))

# Bar plot for Sales
sns.barplot(data=df, x='category', y='Sales', color='blue', label='Sales')

# Line plot for Cumulative Percentage
plt.plot(df['category'], df['CumulativePercentage'], color='red', marker='o', label='Cumulative Percentage')

plt.axhline(y=80, color='green', linestyle='--', label='80% Threshold')  # 80% threshold line

plt.xticks(rotation=90)
plt.title('Pareto Analysis (80/20 Rule) for Products')
plt.xlabel('category')
plt.ylabel('Sales')
plt.legend()
plt.tight_layout()
plt.show()
