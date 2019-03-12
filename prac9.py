import numpy as np
import pandas as pd


df = pd.DataFrame({
    'Col1': [1, 2, 3, 4],
    'Col2': [444, 555, 666, 444],
    'Col3': ['abc', 'def', 'ghi', 'xyx']
})

print(df.head())
print(df)

print(df['Col2'].unique())

# print(len(df['Col2'].unique()))
print(df['Col2'].nunique())

print(df['Col2'].value_counts())

print(df[df['Col1'] > 2])
print(df[(df['Col1'] > 2) & (df['Col2' == 444])])
