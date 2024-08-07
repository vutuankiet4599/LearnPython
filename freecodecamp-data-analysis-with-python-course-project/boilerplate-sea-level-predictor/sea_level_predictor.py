import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    line1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = np.arange(df['Year'].min(), 2050, 1)
    y1 = line1.slope*x1 + line1.intercept

    plt.plot(x1, y1, 'r')

    # Create second line of best fit
    df2000 = df[df['Year'] >= 2000]
    line2 = linregress(df2000['Year'], df2000['CSIRO Adjusted Sea Level'])
    x1 = np.arange(2000, 2050, 1)
    y1 = line2.slope*x1 + line2.intercept

    plt.plot(x1, y1, 'green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
        
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()