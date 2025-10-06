# Week 02 - Classification - Notes

## Data preparation

- `!wget` - Linux shell command for downloading data
- `pd.read.csv()` - read csv files
- `df.head()` - take a look of the dataframe
- `df.head().T` - take a look of the transposed dataframe
- `df.columns` - retrieve column names of a dataframe
- `df.columns.str.lower()` - lowercase all the letters in the columns names of a dataframe
- `df.columns.str.replace(' ', '_')` - replace the space separator in the columns names of a dataframe
- `df.dtypes` - retrieve data types of all series
- `df.index` - retrieve indices of a dataframe
- `pd.to_numeric()` - convert a series values to numerical values. The `errors='coerce'` argument allows making the transformation despite some encountered errors.
- `df.fillna()` - replace NAs with some value
- `(df.x == "yes").astype(int)` - convert x series of yes-no values to numerical values.

## Setting up the validation framework

- `train_test_split` - Scikit-Learn class for splitting a dataset into two parts. The test_size argument states how large the test set should be. The random_state argument sets a random seed for reproducibility purposes.
- `df.reset_index(drop=True)` - reset the indices of a dataframe and delete the previous ones.
- `df.x.values` - extract the values from x series
- `del df['x']` - delete x series from a dataframe

## EAD

- `df.isnull().sum()` - returns the number of null values in the dataframe.
- `df.x.value_counts()` returns the number of values for each category in x series. The `normalize=True` argument retrieves the percentage of each category. 
- `round(x, y)` - round an x number with y decimal places
- `df[x].nunique()` - returns the number of unique values in x series

## Feature importance

- Check the global variable and compare it with the different groups.
    - For example, global churn rate is X; then for gender, check churn rate for `female` and `male`and how they compare with global
    - To compare you can use `global - group` (absolute terms) or `global/group` (relative terms).

- `df.groupby('x').y.agg([mean()])` - returns a dataframe with mean of y series grouped by x series
- `display(x)`-  displays an output in the cell of a jupyter notebook.

## Mutual information
- Concept from information theory,  quantifies the amount of information when can get about one variable if we know about another variable.
- `mutual_info_score(x, y`)` - Scikit-Learn class for calculating the mutual information between the x target variable and y feature.
- `df[x].apply(y)` - apply a y function to the x series of the df dataframe.
- `df.sort_values(ascending=False).to_frame(name='x')` - sort values in an ascending order and called the column as x.

## Correlation

- `df[x].corrwith(y)` - returns the correlation between x and y series.

## One-hot encoding

- `df[x].to_dict(orient='records')` - convert x series to dictionaries, oriented by rows.
- `DictVectorizer().fit_transform(x)`- Scikit-Learn class for one-hot encoding by converting x dictionaries into a sparse matrix. It does not affect the numerical variables.
- `DictVectorizer().get_feature_names()` - return the names of the columns in the sparse matrix.

## Training Logistic Regression with Scikit-Learn

- `LogisticRegression().fit(x)` - Scikit-Learn class for training the logistic regression model.
- `LogisticRegression().coef_[0]` - return the coefficients or weights of the LR model
- `LogisticRegression().intercept_[0]` - return the bias or intercept of the LR model
- `LogisticRegression().predict[x]` - make predictions on the x dataset
- `LogisticRegression().predict_proba[x]` - make predictions on the x dataset by returning two columns with their probabilities for the two categories - soft predictions

## Model interpretation

- You can use the `zip` function together with `dv.get_feature_names_out` to get the coefficient of the features and see which ones mostly impact the model.
- `zip(x,y)` - returns a new list with elements from x joined with their corresponding elements on y
- if we use just the `intercept` with no other information, and apply the `sigmoid` function to it, that is the probability of the event when we know nothing else about the data (the customer data, for example)