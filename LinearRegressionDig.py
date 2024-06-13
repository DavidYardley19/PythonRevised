"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression



Was a bit concerned with the outlier in the first code 'chunk' >>>
    There are 3 main methods to tackle this.
        > Huber Loss Function implementation (Huber linear regression) "Robust regression"
        > Data transformation (Transformation of data, reducing outlier impact)
        > Outlier removal (Before fitting the model)
"""


""" # Step 1: Import the necessary libraries
# (Already done above)

# Step 2: Prepare your data
# For example, let's create a simple dataset
data = {
    'X': [1, 2, 3, 4, 5, 6],
    'y': [2, 3, 5, 7, 11, 99]
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
 """

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, HuberRegressor

# Example data with outliers
X = np.array([1, 2, 3, 4, 4.5, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([1, 2, 1.3, 3.75, -2, 2.25, 5.5, 4.1, 8.9, 7.6, 100])  # Note the outlier at y=100

# Fit a standard linear regression model
lr = LinearRegression()
lr.fit(X, y)
y_pred_lr = lr.predict(X)

# Fit a Huber regressor
huber = HuberRegressor()
huber.fit(X, y)
y_pred_huber = huber.predict(X)

# Plotting the results
plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X, y_pred_lr, color='red', linewidth=2, label='Linear Regression')
plt.plot(X, y_pred_huber, color='green', linewidth=2, label='Huber Regression')
plt.axhline(y=0, color='black', linestyle='--', linewidth=1, label='Horizontal line at y=0')

plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression vs Huber Regression')
plt.legend()
plt.show()
#





#
""" The following uses standard deviation to filter out points before they are fitted to the model """
from scipy.stats import zscore

# Compute Z-scores of y
z_scores = zscore(y)

# Filter out points with Z-score greater than 3 or less than -3
filtered_indices = np.abs(z_scores) < 3
X_filtered = X[filtered_indices]
y_filtered = y[filtered_indices]

# Fit linear regression on filtered data
lr_filtered = LinearRegression()
lr_filtered.fit(X_filtered, y_filtered)
y_pred_filtered = lr_filtered.predict(X_filtered)

# Plotting the results
""" plt.scatter(X, y, color='blue', label='Original Data points') """
plt.scatter(X_filtered, y_filtered, color='cyan', label='Filtered Data points')
plt.plot(X_filtered, y_pred_filtered, color='red', linewidth=2, label='Linear Regression (Filtered)')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression after Outlier Removal')
plt.legend()
plt.show()
