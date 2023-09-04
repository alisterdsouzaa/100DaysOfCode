import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Table_28_07_23.csv', encoding='cp1252')
print(df)

# Example 1: Line Plot
plt.figure(figsize=(10, 6))  # Optional: Set the figure size
plt.plot(df['Torque'], df['Speed'], label='Data Series 1', marker='o', linestyle='-')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Line Plot')
plt.legend()
plt.grid(True)  # Optional: Add grid lines
plt.show()

plt.figure(figsize=(10, 6))  # Optional: Set the figure size
sns.scatterplot(x='Torque', y='Speed', data=df, label='Data Series 2', marker='o')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Scatter Plot')
plt.legend()
plt.grid(True)  # Optional: Add grid lines
plt.show()