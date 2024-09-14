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
SELECT  [YearMonth]
      ,[TotalSales]
      ,[TargetAmount]
      ,[AchievementPercentage]
  FROM [Darina Exam ].[dbo].[PercentageOfGoalAchievement]
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

# Plot 1: Percentage Achievement by Month
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='YearMonth', y='AchievementPercentage', palette='viridis')
plt.xticks(rotation=45)
plt.title('Percentage of Goal Achievement by Month')
plt.xlabel('YearMonth')
plt.ylabel('Achievement Percentage')
plt.tight_layout()
plt.show()

# Plot 2: Cumulative Sales by Year and Month
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='YearMonth', y='TotalSales', marker='o')
plt.xticks(rotation=45)
plt.title('Cumulative Sales by Year and Month')
plt.xlabel('YearMonth')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

# Plot 3: Sales vs Target Amount
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='YearMonth', y='TotalSales', label='Total Sales', marker='o')
sns.lineplot(data=df, x='YearMonth', y='TargetAmount', label='Target Amount', marker='o')
plt.xticks(rotation=45)
plt.title('Sales vs Target Amount')
plt.xlabel('YearMonth')
plt.ylabel('Amount')
plt.legend()
plt.tight_layout()
plt.show()
