import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Import the necessary libraries
# (Already done above)

# Step 2: Prepare your data
# For example, let's create a simple dataset
data = {
    'X': [1, 2, 3, 4, 5],
    'y': [2, 3, 5, 7, 11]
}
df = pd.DataFrame(data)

# Separate the features and target variable
X = df[['X']].values  # Features need to be in 2D array
y = df['y'].values

# Step 3: Fit a linear regression model
model = LinearRegression()
model.fit(X, y)

# Step 4: Make predictions
y_pred = model.predict(X)

# Step 5: Visualize the results
plt.scatter(X, y, color='blue', label='Original Data')
plt.plot(X, y_pred, color='red', linewidth=2, label='Linear Regression Line')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression Example')
plt.legend("This is a test")
plt.show()
