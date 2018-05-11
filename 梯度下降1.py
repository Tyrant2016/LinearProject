import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# 获取数据文件
data = pd.read_csv(os.path.join(os.getcwd(), 'Datas', 'Data-Cleaning-2.csv'))

# 这里要开始做的就是线性回归的梯度下降
