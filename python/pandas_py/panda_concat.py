import pandas as pd
# creating the Series
series1 = pd.Series([1, 2, 3])
print('series1:', series1)
series2 = pd.Series(['A', 'B', 'C'])
print('series2:', series2)
# concatenating
print('After concatenating:')
print(pd.concat([series1, series2]))