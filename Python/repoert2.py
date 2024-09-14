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
SELECT TOP (1000) [Year]
      ,[Month]
      ,[CumulativeSales]
  FROM [Darina Exam].[dbo].[CumulativeSalesByYearAndMonth]
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

# Combine Year and Month into a YearMonth column
df['YearMonth'] = df['Year'].astype(str)

# Ensure YearMonth is treated as string and sort by YearMonth
df = df.sort_values('YearMonth')

# Set the style of seaborn
sns.set(style="whitegrid")

# Plot: Cumulative Sales by Year and Month
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='YearMonth', y='CumulativeSales', marker='o')
plt.xticks(rotation=45)
plt.title('Cumulative Sales by Year and Month')
plt.xlabel('Year-Month')
plt.ylabel('Cumulative Sales')
plt.tight_layout()
plt.show()
