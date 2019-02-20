import numpy as np
import pandas as pd


d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
df = pd.DataFrame(d)
print(df)

# axis 0은 Rows, 1은 columns / thresh는 non-nan값의 갯수 / inplace 잊지 말기
df.dropna(thresh=3)
print(df)

# 모든 nan값을 채워줌
df.fillna(value='None value')
print(df)

# fillna = Nan값을 채움. value parameter를 설정해줘야 함.
df['A'].fillna(value=df['A'].mean())
print(df)
