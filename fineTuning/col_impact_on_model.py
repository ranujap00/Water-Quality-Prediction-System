import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import pandas as pd
import joblib

df = pd.read_csv('Water Quality Prediction.csv')
df = df.sample(n=100000, random_state=42)

# remove all rows with Nan values
df.dropna(inplace=True) # modifies the dataframe in place

encoded_data = pd.get_dummies(df, columns=['Color'])

X = encoded_data.drop(['Potability', 'Index', 'Lead', 'Month', 'Source'], axis=1) # axis=1 indicates we are dropping a column, not a row
Y = encoded_data['Potability']

# Assuming X contains your feature columns and y contains 'Potability'
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Create and train the Random Forest classifier
rfc_classifier = RandomForestClassifier(n_estimators = 100, criterion='entropy', random_state = 0)
rfc_classifier.fit(X_train, y_train)


# Make predictions on the test set
y_pred = rfc_classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Get feature importances
feature_importances = rfc_classifier.feature_importances_

features = []
importances = []
# Print or visualize feature importances
for feature_name, importance in zip(X.columns, feature_importances):
    print(f"{feature_name}: {importance}")
    features.append(feature_name)
    importances.append(importance)


# Create a bar chart
plt.figure(figsize=(12, 6))
plt.barh(features, importances)
plt.xlabel('Feature Importance')
plt.title('Feature Importances')
plt.gca().invert_yaxis()
plt.show()