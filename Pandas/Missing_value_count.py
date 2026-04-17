import pandas as pd
# Assume 'df' is your DataFrame
# Create a sample DataFrame for demonstration
data = {'Feature_A': [1, 2, None, 4, 5], 
        'Feature_B': ['X', 'Y', 'Z', None, 'W'],
        'Feature_C': [10.1, None, 30.3, 40.4, 50.5]}
df = pd.DataFrame(data)

# Check the total count of missing values per column
print("Missing Value Counts:")
print(df.isnull().sum())
M= df["Feature_A"].fillna(df["Feature_A"].mean(), inplace=True)
#N= df["Feature_B"].fillna(df["Feature_B"].median(),inplace=True)
K= df["Feature_C"].fillna(df["Feature_C"].mode(), inplace=True)
print(df)
