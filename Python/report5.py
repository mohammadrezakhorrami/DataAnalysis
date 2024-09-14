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
      ,[category]
      ,[TotalProductShare]
  FROM [Darina Exam].[dbo].[SalesShareOfEachProductByYear]
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

# Set the style of seaborn
sns.set(style="whitegrid")

# Plot: Sales Share of Each Product by Year
plt.figure(figsize=(14, 8))
sns.barplot(data=df, x='Year', y='TotalProductShare', hue='category', palette='viridis')
plt.xticks(rotation=45)
plt.title('Sales Share of Each Product by Year')
plt.xlabel('Year')
plt.ylabel('Total Product Share (%)')
plt.legend(title='Product Category')
plt.tight_layout()
plt.show()
