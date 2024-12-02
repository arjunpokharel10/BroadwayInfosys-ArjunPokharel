import numpy as np
import pandas as pd

df = pd.read_csv('/Users/pokharel/Projects/Python/DataAnalysis/sample_df.txt', delimiter='\t')

mask = df['Room number'].isna()
df['Text Value'] = np.where(mask, df['Date'],np.nan)
df['Text Value'].fillna(method='bfill', inplace=True)
df.dropna(inplace=True)

print(df.head())



