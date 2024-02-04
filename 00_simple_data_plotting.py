# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# "data/advertising.csv" containts the data set used in this exercise
data_filename = 'data/advertising.csv'

# Read the file "Advertising.csv" file using the pandas library
df = pd.read_csv(data_filename)

# Quick look at the data, looking at the first 5 rows with the column names
df.head()

# Returns subset of the df that is contained in the row range used as argument
# + print to see if selection worked
df_new = df.iloc[:7]
print(df_new)


# Use a scatter plot for plotting a graph of TV vs Sales
plt.scatter(df["TV"], df["Sales"])

# Add axis labels for clarity (x : TV budget, y : Sales)
plt.xlabel("TV budget")
plt.ylabel("Sales")

# Add plot title
plt.title("Prediction")

# Display the plot
plt.show()

# use to organise the data, when the data is not organised
# alternative np arrange
# generate a range of evenly spaced values for x-coordinates
# x_values = np.linspace(0, 10, 500, endpoint=True)

