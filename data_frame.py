import numpy as np
import pandas as pd

#
from numpy.random import randn

np.random.seed(101)
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

# print(df)
# # print(df['W'])
# print(df[['W', 'Y']])

df['new'] = df['W'] + df['Y']
# print(df)
#
# df.drop('new', axis=1, inplace=True)  ## without inplace change will not be permanent
# print(df)

# print(df.loc['A'])
# print(df.iloc[2])
# print(df.loc['C', 'Y'])
# print(df.loc[['A', 'B'], ['X', 'Y']])
# print(df)
#
# print(df > 0)
# print(df[df['W'] > 0])

# booldf = df['W'] > 0
# # print(booldf)
# mycols = [df['Y'], df['X']]
# print(mycols)
# # ------- missing values ---------

d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
df = pd.DataFrame(d)
# print(df)

# print(df.dropna())
# print(df.dropna(axis=1))
# print(df.dropna(thresh=2))
# print(df.fillna(value='fill'))
# print(df['A'].fillna(value=df['A'].mean()))
