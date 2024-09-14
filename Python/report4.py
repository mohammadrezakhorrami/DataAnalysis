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
SELECT [Year]
      ,[Month]
      ,[YearMonth]
      ,[CurrentYearSales]
      ,[PreviousYearSales]
      ,[YoYGrowth]
  FROM [Darina Exam].[dbo].[SalesYearlyComparison]
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

# Ensure YearMonth is treated as a string and sort by YearMonth
df['YearMonth'] = df['YearMonth'].astype(str)
df = df.sort_values('YearMonth')

# Set the style of seaborn
sns.set(style="whitegrid")

# Plot 1: Sales Comparison (Current Year vs Previous Year)
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='YearMonth', y='CurrentYearSales', marker='o', label='Current Year Sales')
sns.lineplot(data=df, x='YearMonth', y='PreviousYearSales', marker='o', label='Previous Year Sales')
plt.xticks(rotation=45)
plt.title('Sales Comparison: Current Year vs Previous Year')
plt.xlabel('Year-Month')
plt.ylabel('Sales')
plt.legend()
plt.tight_layout()
plt.show()

# Plot 2: Year-over-Year Growth
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='YearMonth', y='YoYGrowth', palette='viridis')
plt.xticks(rotation=45)
plt.title('Year-over-Year Growth')
plt.xlabel('Year-Month')
plt.ylabel('YoY Growth (%)')
plt.tight_layout()
plt.show()
