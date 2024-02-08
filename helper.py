# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

# Read the file "Advertising.csv"
df = pd.read_csv("Advertising.csv")

# Set 'Sales' as the predictor variable
y = df['Sales']


# Function to fit a linear model on the predictor passed as a parameter, compute the parameters
# and plot the fit of the R^2
def fit_and_plot_linear(x):

	# Split the data into train and test sets with train size of 0.8
	# Set the random state as 0 to get reproducible results
	x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.8,random_state=0)

	# Initialize a LinearRegression object
	lreg = LinearRegression()

	# Fit the model on the train data
	lreg.fit(x_train, y_train)

	# Predict the response variable of the train set using the trained model
	y_train_pred = lreg.predict(x_train)

	# Predict the response variable of the test set using the trained model
	y_test_pred= lreg.predict(x_test)

	# Compute the R-square for the train predictions
	r2_train = r2_score(y_train, y_train_pred)

	# Compute the R-square for the test predictions
	r2_test = r2_score(y_test, y_test_pred)

	# Code to plot the prediction for the train and test data
	plt.scatter(x_train, y_train, color='#B2D7D0', label = "Train data")
	plt.scatter(x_test, y_test, color='#EFAEA4', label = "Test data")
	plt.plot(x_train, y_train_pred, label="Train Prediction", color='darkblue', linewidth=2)
	plt.plot(x_test, y_test_pred, label="Test Prediction", color='k', alpha=0.8, linewidth=2, linestyle='--')
	name = x.columns.to_list()[0]
	plt.title(f"Plot to indicate linear model predictions")
	plt.xlabel(f"{name}", fontsize=14)
	plt.ylabel("Sales", fontsize=14)
	plt.legend()
	plt.show()

	# Return the r-square of the train and test data
	return r2_train, r2_test



# Function to fit a multilinear model on all the predictors in the dataset passed as a parameter, compute the parameters
# and plot the fit of the R^2
def fit_and_plot_multi():

	# Get the predictor variables
	x = df[['TV','Radio','Newspaper']]

	# Split the data into train and test sets with train size of 0.8
	# Set the random state as 0 to get reproducible results
	x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=0.8,random_state=0)

	# Initialize a LinearRegression object to perform Multi-linear regression
	lreg = LinearRegression()

	# Fit the model on the train data
	lreg.fit(x_train, y_train)

	# Predict the response variable of the train set using the trained model
	y_train_pred = lreg.predict(x_train)

	# Predict the response variable of the test set using the trained model
	y_test_pred= lreg.predict(x_test)

	# Compute the R-square for the train predictions
	r2_train = r2_score(y_train, y_train_pred)

	# Compute the R-square for the test predictions
	r2_test = r2_score(y_test, y_test_pred)

	# Return the r-square of the train and test data
	return r2_train, r2_test


def get_poly_pred(x_train, x_test, y_train, degree=1):

    # Generate polynomial features on the train data
    x_poly_train= PolynomialFeatures(degree=degree).fit_transform(x_train)

    # Generate polynomial features on the test data
    print(x_train.shape, x_test.shape, y_train.shape)
    x_poly_test= PolynomialFeatures(degree=degree).fit_transform(x_test)

    # Initialize a model to perform polynomial regression
    polymodel = LinearRegression()

    # Fit the model on the polynomial transformed train data
    polymodel.fit(x_poly_train, y_train)

    # Predict on the entire polynomial transformed test data
    y_poly_pred = polymodel.predict(x_poly_test)
    return y_poly_pred
