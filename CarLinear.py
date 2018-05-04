import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
import os

from statsmodels.distributions.empirical_distribution import ECDF
from sklearn.metrics import mean_squared_error, r2_score

# machine learning
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso, LassoCV
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor

seed = 123

# import data (? = missing values)
"""
数据集简介,主要包括3类指标:

汽车的各种特性.
保险风险评级：(-3, -2, -1, 0, 1, 2, 3).
每辆保险车辆年平均相对损失支付.

类别属性
make: 汽车的商标（奥迪，宝马。。。）
fuel-type: 汽油还是天然气
aspiration: 涡轮
num-of-doors: 两门还是四门
body-style: 硬顶车、轿车、掀背车、敞篷车
drive-wheels: 驱动轮
engine-location: 发动机位置
engine-type: 发动机类型
num-of-cylinders: 几个气缸
fuel-system: 燃油系统

连续指标
bore: continuous from 2.54 to 3.94.
stroke: continuous from 2.07 to 4.17.
compression-ratio: continuous from 7 to 23.
horsepower: continuous from 48 to 288.
peak-rpm: continuous from 4150 to 6600.
city-mpg: continuous from 13 to 49.
highway-mpg: continuous from 16 to 54.
price: continuous from 5118 to 45400.
"""
data_path = os.path.join(os.getcwd(), 'Datas', 'Auto-Data.csv')
data = pd.read_csv(data_path, na_values='?')
# check datas
# print(data.columns)
"""
['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration',
       'num-of-doors', 'body-style', 'drive-wheels', 'engine-location',
       'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-type',
       'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke',
       'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg',
       'highway-mpg', 'price']
"""
# print(data.dtypes)
"""
symboling              int64
normalized-losses     object
make                  object
fuel-type             object
aspiration            object
num-of-doors          object
body-style            object
drive-wheels          object
engine-location       object
wheel-base           float64
length               float64
width                float64
height               float64
curb-weight            int64
engine-type           object
num-of-cylinders      object
engine-size            int64
fuel-system           object
bore                  object
stroke                object
compression-ratio    float64
horsepower            object
peak-rpm              object
city-mpg               int64
highway-mpg            int64
price                 object
"""
# print("In Total: ",data.shape)
# In Total:  (205, 26)
# check "count mean std max min"
# print(data.describe())

# How to solve the missing-value?
"""
1.if the missing-value is small porpotion in all datas(like 1%), Delete the item includes missing-value.
2.use the mean replace the missing-value.
3.use regession model to fix it.
"""


