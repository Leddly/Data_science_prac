from numpy.random import randn
import numpy as np
import pandas as pd


np.random.seed(101)

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

print(hier_index)

df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])
print(df)

print(df.loc['G1'].loc[1])

# [outside, inside]
df.index.names = ['Groups', 'Num']
print(df)

print(df.loc['G2'].loc[2])

# Return Cross-section of rows and columns in multi level index
print(df.xs('G1'))
# = print(df.loc['G1'])

# level = index_name
print(df.xs(1, level='Num'))
print(df.xs(2, level='Num'))
print(df.xs(3, level='Num'))
print(df.xs())
