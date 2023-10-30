# %%
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# %%
df = pd.read_csv('D:\\SLIIT\\Year 03 sem 02\\FDM\\Mini-project-updated-version\\FDM_Mini_Project\\backend\\Water Quality Prediction.csv')
df = df.sample(n=100000, random_state=42)

# %%
df.dropna(inplace=True)

# %%
selected_features = df[['pH', 'Iron', 'Nitrate', 'Chloride', 'Turbidity', 'Fluoride', 'Copper', 'Odor', 'Sulfate', 'Conductivity', 'Chlorine', 'Manganese', 'Total Dissolved Solids', 'Water Temperature', 'Air Temperature', 'Day']]
X = selected_features.to_numpy()

# %%
# Determine the optimal number of clusters using the Elbow Method
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Plot the WCSS values
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS')
plt.show()

# %%
# Choose the optimal number of clusters (e.g., 3, 4, etc.) based on the Elbow Method
optimal_k = 3

# Perform K-Means clustering
kmeans = KMeans(n_clusters=optimal_k, init='k-means++', max_iter=300, n_init=10, random_state=0)
cluster_assignments = kmeans.fit_predict(X)

# Add the cluster assignments to your DataFrame
df['Cluster'] = cluster_assignments

# %%
# Visualize the clusters (example for two features: pH and iron)
# plt.scatter(X[:, 0], X[:, 2], c=cluster_assignments, cmap='rainbow')
# plt.title('K-Means Clustering')
# plt.xlabel('pH')
# plt.ylabel('Iron')
# plt.show()

feature_pairs = [('pH', 'Potability'), ('pH', 'Chloride'), ('pH', 'Turbidity')]
for feature1, feature2 in feature_pairs:
    plt.scatter(df[feature1], df[feature2], c=cluster_assignments, cmap='rainbow')
    plt.title(f'K-Means Clustering: {feature1} vs. {feature2}')
    plt.xlabel(feature1)
    plt.ylabel(feature2)
    plt.show()

# %%
values = [1, 7.06e-08, 1.31e-95,
       0.767179279, 0.137766996, 1.008886456, 2.391833449,
       0.750761234, 148.9474344, 242.7039915, 3.709734571, 2.301398715,
       100.9851033, 9.674425593, 1.0]



# %%
# Predict the cluster for the single input
predicted_cluster = kmeans.predict([values])

print(f"The single input belongs to Cluster {predicted_cluster[0]}")


