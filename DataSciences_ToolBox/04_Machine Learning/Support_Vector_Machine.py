# Title: Support Vector Machines (SVM) for Regression and Classification

# Purpose: This script demonstrates how to use Support Vector Machines (SVM) for:
# 1. Linear regression on time series data (Google stock prices).
# 2. Classification on the Iris dataset.

import pandas as pd
from pandas_datareader import data as pdr
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.svm import SVR, SVC  # Support Vector Regression & Classification
from sklearn.metrics import r2_score, mean_squared_error, confusion_matrix, classification_report
import numpy as np



# Section 1: Linear SVM for Regression (Google Stock Prices)

# Fetch Google stock data
symbol = 'GOOG'
start_date = pd.to_datetime('today') - pd.DateOffset(years=5)
end_date = pd.to_datetime('today')
data = pdr.get_data_yahoo(symbol, start=start_date, end=end_date)

# Prepare data for regression
df = data[['Open', 'High', 'Low', 'Close', 'Volume', 'Adjusted']].copy()
df.dropna(inplace=True)  # Drop any rows with missing values

X = df.drop(columns=['Close'])  
y = df['Close'] 

# Split the data into training (70%) and validation (30%) sets
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.3, random_state=7)

# Train the Linear SVM Regression model
model = SVR(kernel='linear') 

# Cross-validation
cv_results = cross_validate(model, X_train, y_train, cv=10, scoring='r2')
print(f"\nLinear SVM Regression Cross-Validation Results:\nMean R-squared: {cv_results['test_score'].mean():.4f}")

# Fit the model
model.fit(X_train, y_train)

# Make predictions on the validation set
y_pred = model.predict(X_valid)

# Evaluate the model
r2 = r2_score(y_valid, y_pred)
mse = mean_squared_error(y_valid, y_pred)

print(f"\nLinear SVM Regression Metrics:\nR-squared: {r2:.4f}\nMean Squared Error: {mse:.4f}")





# Section 2: Linear SVM for Classification (Iris Dataset)
# Load the Iris dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# Split the data into training (70%) and validation (30%) sets
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.3, random_state=7)

# Train the Linear SVM classifier 
clf = SVC(kernel='linear', random_state=7)  # Using a linear kernel

# Cross-validation
cv_results = cross_validate(clf, X_train, y_train, cv=10, scoring='accuracy')
print(f"\nLinear SVM Classification Cross-Validation Results:\nMean Accuracy: {cv_results['test_score'].mean():.4f}")


# Fit the model
clf.fit(X_train, y_train)

# Make predictions on the validation set
y_pred = clf.predict(X_valid)

# Evaluate the model
confusion_mat = confusion_matrix(y_valid, y_pred)
class_report = classification_report(y_valid, y_pred, target_names=iris.target_names)
print("\nLinear SVM Confusion Matrix:")
print(confusion_mat)
print("\nClassification Report:")
print(class_report)
