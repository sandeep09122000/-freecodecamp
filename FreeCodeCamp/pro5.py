
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def load_data():
    # Load the dataset
    df = pd.read_csv('epa-sea-level.csv')
    return df

def plot_sea_level_trends():
    df = load_data()

    # Scatter plot of all data
    plt.figure(figsize=(10,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data points', alpha=0.5)

    # Linear regression using all data
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Generate years for the line: from earliest to 2050
    years_extended = pd.Series(range(df['Year'].min(), 2051))
    sea_level_fit = intercept + slope * years_extended

    # Plot the line of best fit through all data
    plt.plot(years_extended, sea_level_fit, color='red', label='Fit: all data')

    # Linear regression using data from 2000 onward
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    # Generate years for recent fit line: from 2000 to 2050
    years_recent = pd.Series(range(2000, 2051))
    sea_level_recent_fit = intercept_recent + slope_recent * years_recent

    # Plot the recent trend line
    plt.plot(years_recent, sea_level_recent_fit, color='blue', linestyle='--', label='Fit: 2000 onwards')

    # Prediction for 2050
    sea_level_2050_all = intercept + slope * 2050
    sea_level_2050_recent = intercept_recent + slope_recent * 2050

    # Add annotation for predicted sea levels in 2050
    plt.scatter(2050, sea_level_2050_all, color='red')
    plt.scatter(2050, sea_level_2050_recent, color='blue')
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.tight_layout()

    # Save and return the figure
    fig = plt.gcf()
    return fig

# For testing purposes
if __name__ == '__main__':
    fig = plot_sea_level_trends()
    plt.show()