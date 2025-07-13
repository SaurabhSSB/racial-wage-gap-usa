# perform linear operations
import numpy as np
# Data manipulation
import pandas as pd
# Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns
# Remove warnings
import warnings
warnings.filterwarnings('ignore')
# Perfrom Stastical operation
from scipy.stats import ttest_ind

# Load the dataset
black_white = pd.read_csv(r"C:\Users\Lenovo\Downloads\content\Black-White Wage Gap Data Analysis\black_white_wage_gap.csv")
# Print top 5 rows
black_white.head()

# Print last 5 rows
black_white.tail()
black_white.shape

# Check info of each colummn
black_white.info()

# check for duplicate
black_white.duplicated().sum()

black_white['year'].unique()

plt.figure(figsize=(12, 8))
# Overall median wages
plt.plot(black_white['year'], black_white['white_median'], label='White Median', linestyle='--', marker='o')
plt.plot(black_white['year'], black_white['black_median'], label='Black Median', linestyle='--', marker='o')
# Overall average wages
plt.plot(black_white['year'], black_white['white_average'], label='White Average', linestyle='-', marker='x')
plt.plot(black_white['year'], black_white['black_average'], label='Black Average', linestyle='-', marker='x')
plt.title('Overall Median and Average Wages Over Time')
plt.xlabel('Year')
plt.ylabel('Wage')
plt.legend()
plt.grid(True)
plt.show()

# Calculate the wage gap
black_white['wage_gap'] = black_white['white_median'] - black_white['black_median']
# Line chart for the wage gap over time
plt.figure(figsize=(12, 8))
plt.plot(black_white['year'], black_white['wage_gap'], label='Wage Gap', marker='o', linestyle='--', color='red')
plt.title('Wage Gap Between White and Black Workers Over Time')
plt.xlabel('Year')
plt.ylabel('Wage Gap')
plt.axhline(y=0, color='black', linestyle='--', linewidth=0.8, label='Zero Gap')
plt.legend()
plt.grid(True)
plt.show()

# Calculate the wage gap for men and women separately
black_white['wage_gap_men'] = black_white['white_men_median'] - black_white['black_men_median']
black_white['wage_gap_women'] = black_white['white_women_median'] - black_white['black_women_median']
# Line chart for the wage gap for men and women over time
plt.figure(figsize=(12, 8))
plt.plot(black_white['year'], black_white['wage_gap_men'], label='Wage Gap (Men)', marker='o', linestyle='--', color='blue')
plt.plot(black_white['year'], black_white['wage_gap_women'], label='Wage Gap (Women)', marker='x', linestyle='--', color='green')
plt.title('Wage Gap Between White and Black Men and Women Over Time')
plt.xlabel('Year')
plt.ylabel('Wage Gap')
plt.axhline(y=0, color='black', linestyle='--', linewidth=0.8, label='Zero Gap')
plt.legend()
plt.grid(True)
plt.show()

years = black_white['year'].unique()
for subgroup in ['white_men', 'black_men', 'white_women', 'black_women']:
    median_p_values = []
    average_p_values = []
    for year in years:
        # Subset data for the specific year and subgroup
        subset_data = black_white[black_white['year'] == year]
        white_values = subset_data[f'{subgroup}_median']
        black_values = subset_data[f'{subgroup}_median']
        # Perform t-test for median wages
        _, median_p_value = ttest_ind(white_values, black_values, equal_var=False)
        median_p_values.append(median_p_value)
        # Perform t-test for average wages
        white_values = subset_data[f'{subgroup}_average']
        black_values = subset_data[f'{subgroup}_average']
        _, average_p_value = ttest_ind(white_values, black_values, equal_var=False)
        average_p_values.append(average_p_value)
    # Visualize p-values over the years
    plt.figure(figsize=(12, 8))
    plt.plot(years, median_p_values, label='Median Wage p-values', marker='o', linestyle='--')
    plt.plot(years, average_p_values, label='Average Wage p-values', marker='x', linestyle='--')
    plt.title(f'Significance of Changes in {subgroup.capitalize()} Wages Over Time')
    plt.xlabel('Year')
    plt.ylabel('p-value')
    plt.axhline(y=0.05, color='red', linestyle='--', linewidth=0.8, label='Significance Level (0.05)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Filter data for the past decade
start_year = black_white['year'].max() - 10
recent_data = black_white[black_white['year'] >= start_year]
# Calculate the wage gap
recent_data['wage_gap'] = recent_data['white_median'] - recent_data['black_median']
# Line chart for the wage gap over the past decade
plt.figure(figsize=(12, 8))
plt.plot(recent_data['year'], recent_data['wage_gap'], label='Wage Gap', marker='o', linestyle='--', color='red')
plt.title('Wage Gap Over the Past Decade')
plt.xlabel('Year')
plt.ylabel('Wage Gap')
plt.axhline(y=0, color='black', linestyle='--', linewidth=0.8, label='Zero Gap')
plt.legend()
plt.grid(True)
plt.show()

# Filter data for recent years
recent_data = black_white[black_white['year'] >= 2015]
# Line chart for median and average wages comparison
plt.figure(figsize=(12, 5))
# Median wages
plt.plot(recent_data['year'], recent_data['white_median'], label='White Median', marker='o', linestyle='--', color='red')
plt.plot(recent_data['year'], recent_data['black_median'], label='Black Median', marker='x', linestyle='--', color='orange')
# Average wages
plt.plot(recent_data['year'], recent_data['white_average'], label='White Average', marker='o', linestyle='-', color='blue')
plt.plot(recent_data['year'], recent_data['black_average'], label='Black Average', marker='x', linestyle='-', color='green')
plt.title('Comparison of Median and Average Wages for White and Black Workers (Recent Years)')
plt.xlabel('Year')
plt.ylabel('Wage')
plt.legend()
plt.grid(True)
plt.show()
