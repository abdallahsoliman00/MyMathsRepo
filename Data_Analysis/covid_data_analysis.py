import matplotlib.pyplot as plt
import pandas as pd

from Numerical_Solutions.Linear_regression import grad_descent


# Read data
data_path  =r'MyMathsRepo\supplementary_data\WHO-COVID-19-global-data.csv'
data = pd.read_csv(data_path)


# Sort by date
data['Date_reported'] = pd.to_datetime(data['Date_reported'])
data = data.sort_values('Date_reported')


# Clean data
data = data.drop(["Country_code", "Country", "WHO_region", "New_deaths", "Cumulative_deaths"], axis=1)
data = data.groupby('Date_reported', as_index=False).sum(numeric_only=True)


# Plot
dates = pd.to_datetime(data['Date_reported'])
new_cases = data['New_cases']
cumulative_cases = data['Cumulative_cases']

