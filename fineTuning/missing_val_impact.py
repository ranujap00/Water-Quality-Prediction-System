import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import f1_score

df = pd.read_csv('Water Quality Prediction.csv')
df = df.sample(n=100000, random_state=42)

# remove all rows with Nan values
# df.dropna(inplace=True) # modifies the dataframe in place

encoded_data = pd.get_dummies(df, columns=['Color', 'Month'])

X = encoded_data.drop(['Potability', 'Index', 'Lead', 'Source', 'Time of Day', 'Zinc'], axis=1) # axis=1 indicates we are dropping a column, not a row
Y = encoded_data['Potability']

print(X)

imputer = SimpleImputer(missing_values=np.nan, strategy='median')
imputer.fit(X)
X = imputer.transform(X)  # returns the updated columns

# Assuming X contains your feature columns and y contains 'Potability'
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Create and train the Random Forest classifier
rfc_classifier = RandomForestClassifier(n_estimators = 100, criterion='entropy', random_state = 0)
rfc_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rfc_classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("F1 Score:", f1)

print("Precision:", precision)
print("Recall:", recall)


### accuracy 

# remove missing values - 0.8618007777445408
# replace with the mean - 0.86755
# replace with the median - 0.8681 (BEST ONE)
# replace with the most_frequent - 0.8662
# replace with the constant - 0.86605
