import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']

numArr = np.array([10, 20, 30])

dtnry = {'a': 10, 'b': 20, 'c': 30}

# print(pd.Series(labels))
# print(pd.Series(numArr))
# print(pd.Series(dtnry))

s = pd.Series(numArr, labels)
print(s)
