import pandas as pd
MyCases = pd.read_csv('Covidcases.csv')
print(MyCases)

MyCases['Date'] = pd.to_datetime(MyCases['Date'], format='%Y-%m-%d')

# Filter data between two dates
filtered_df = MyCases.loc[(MyCases['Date'] >= '2020-09-01')
                     & (MyCases['Date'] < '2020-09-15')]
# Display
print(filtered_df)