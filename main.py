import pandas as pd

# Read dataset and convert into dataframe
data = pd.read_csv('data/california_housing_train.csv')

# Show first five row of dataset
print(data.head())
