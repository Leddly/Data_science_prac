import numpy as np
import pandas as pd


data = {
    'Company': ['Goog', 'Goog', 'Msft', 'Msft', 'Fb', 'Fb'],
    'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
    'Sales': [200, 120, 340, 124, 243, 350]
}

df = pd.DataFrame(data)
print(df)

by_comp = df.groupby('Company')

print(by_comp.mean())
print(by_comp.std())
print(by_comp.sum().loc['Fb'])
# transpose는 표의 모양을 바꾸는 것
print(by_comp.describe().transpose())
