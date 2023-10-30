import pandas as pd
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('F:\\SLIIT\Year 03 sem 02\\FDM\\FDM_Updated_project\\FDM_Mini_Project_G07\\backend\\Water Quality Prediction.csv')
df = df.drop(['Index', 'Source', 'Zinc', 'Lead', 'Time of Day', 'Potability'], axis=1)


numeric_columns = df.select_dtypes(include=['number'])

min_values = numeric_columns.min()
max_values = numeric_columns.max()

print("Minimum Values:")
print(min_values)
print("\nMaximum Values:")
print(max_values)

# Calculate the correlation matrix
correlation_matrix = numeric_columns.corr()

# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# Create a heatmap
# plt.figure(figsize=(12, 8))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
# plt.title('Correlation Heatmap')
# plt.show()

copper_column = numeric_columns["Copper"]
chloride_column = numeric_columns["Chloride"]

# Calculate the correlation between "Copper" and "Chloride"
correlation = copper_column.corr(chloride_column)

# Create a bar plot to represent the correlation
plt.figure(figsize=(6, 4))
plt.bar(['Copper vs. Chloride'], [correlation], color='b')
plt.title('Correlation between Copper and Chloride')
plt.ylabel('Correlation Coefficient')
plt.ylim(-1, 1)  # Set the y-axis limit to -1 to 1 for correlation values
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()