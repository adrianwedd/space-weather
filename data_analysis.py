
import pandas as pd

def basic_data_analysis(dataframe):
    # Get basic statistics
    statistics = dataframe.describe()
    
    # Find correlations between variables
    correlations = dataframe.corr()
    
    return statistics, correlations

# Sample usage
if __name__ == "__main__":
    # Create a sample dataframe
    df = pd.DataFrame({
        'Temperature': [32, 45, 50, 38, 43],
        'Humidity': [80, 60, 75, 90, 85]
    })
    
    statistics, correlations = basic_data_analysis(df)
    print("Statistics:\n", statistics)
    print("Correlations:\n", correlations)
