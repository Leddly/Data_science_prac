import numpy as np
import pandas as pd
from numpy.random import randn


lables = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}

np.random.seed(101)

print(pd.Series(data=my_data))

print(pd.Series(data=my_data, index=lables))
# print(pd.Series(arr, lables))
# print(pd.Series(my_data, lables))

ser1 = pd.Series([1, 2, 3, 4, 5], ['USA', 'KOR', 'JAP', 'VIT', 'THA'])
print(ser1)
print(ser1['USA'])

ser2 = pd.Series([1, 2, 5, 4], ['USA', 'KOR', 'JAP', 'VIT'])
print(ser2)

ser3 = pd.Series(data=lables)
print(ser3[0])

newser = ser1 + ser2
print(newser)

# print(np.random.seed(101))
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)

print(df['W'])
# print(df.W)

print(df[['W', 'Z']])

df['new'] = df['W'] + df['Y']
print(df)

# Index의 axis값은 0, Column의 axis값은 1 / inplace값을 안 주면 실제 Frame에는 영향이 없음
df.drop('new', axis=1, inplace=True)
print(df)
df.drop('E', axis=0)
print(df)

print(df.shape)

print(df.loc['A'])
print(df.iloc[0])
print(df.iloc[:2])

print(df.loc['B', 'Y'])
print(df.loc[['A', 'B'], ['X', 'Y']])
print(df.iloc[:2, [1, 2]])

print(df > 0)
print(df[df > 0])

print(df['W'] > 0)
print(df[df['W'] > 0])

print(df['Z'])
print(df[df['Z'] < 0])

print(df[df['W'] > 0]['X'])
print(df[df['W'] > 0][['X', 'Y']])

print(df[(df['W'] > 0) & (df['Y'] > 1)])
print(df[(df['W'] > 0) | (df['Y'] > 1)])

# inplace값을 줘야 변함
print(df.reset_index())
print(df)

newindex = 'CA NY WY OR CO'.split()
print(newindex)

df['States'] = newindex

print(df)

# inplace는 필수
df.set_index('States', inplace=True)

print(df)
