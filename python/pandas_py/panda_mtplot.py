import pandas as pd
import matplotlib.pyplot as plt
import math
df = pd.read_csv('data.csv')
print(df)
#filter data
df_filtered=df[df['math']>90]
df_filtered['Name'].value_counts().plot(kind='bar')
plt.title('name disturabation')
plt.xlabel('Name')
plt.ylabel('count')
plt.show()