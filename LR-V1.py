import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import StandardScaler

a = pd.DataFrame([1,2,3])
print(a)
a.insert(1,'bias',1)
print(a)
l=[1,2,3,4]
print(l[len(l)-1])