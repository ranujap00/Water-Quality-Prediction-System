# %%
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer


df = pd.read_csv('Water Quality Prediction.csv')

# df = df.sample(n=200000, random_state=42)


# check for duplicate rows
duplicate_rows = df[df.duplicated()]
if duplicate_rows.count().sum() == 0:
   print("No duplicate rows")
else:
   print("Duplicate rows are present")


df = df.drop(['Index', 'Source', 'Zinc', 'Lead', 'Time of Day'], axis=1)# axis=1 indicates we are dropping a column, not a row


# drop rows with null values in color and source columns
df = df.dropna(subset=["Color", "Month"])


# Identify the numeric columns
numeric_columns = df.select_dtypes(include=['number']).columns

# Create a SimpleImputer and apply it to the numeric columns
imputer = SimpleImputer(strategy='median')  # You can choose a different strategy if needed
df[numeric_columns] = imputer.fit_transform(df[numeric_columns])


# we need x, y values as numpy arrays
X = df.iloc[:, 0:-1].values
Y = df.iloc[:, -1].values

# Label Encode categorical values (1, 2, 3 ... values)
le1 = LabelEncoder()
X[:, 4] = le1.fit_transform(X[:, 4])

le2 = LabelEncoder()
X[:, 16] = le2.fit_transform(X[:, 16])



# Column transform categorical columns (0, 1, 0 ...)
ct1 = ColumnTransformer(transformers=[('encode', OneHotEncoder(), [4])], remainder='passthrough')
X = ct1.fit_transform(X)

ct2 = ColumnTransformer(transformers=[('encode', OneHotEncoder(), [20])], remainder='passthrough')
X = ct2.fit_transform(X)


# Splitting the data set
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)


# Normalize input values

sc = StandardScaler()  # range: -3 to +3
x_train[:, 17:] = sc.fit_transform(x_train[:, 17:])
x_test[:, 17:] = sc.transform(x_test[:, 17:])

print("X TRAIN", x_train[0])
print("Y TRAIN", y_train)

print(x_test)