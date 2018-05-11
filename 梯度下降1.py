import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# 获取数据文件(已清洗)
data = pd.read_csv(os.path.join(os.getcwd(), 'Datas', 'Data-Cleaning-1.csv'))

# 然后先把连续数值数据标准化
standard_scaler = StandardScaler()
features = data.drop('price', axis=1)
continue_columns = ['symboling', 'normalized-losses', 'volume',
                    'horsepower', 'bore', 'stroke', 'compression-ratio',
                    'peak-rpm', 'highway-mpg', 'engine-size']
features[continue_columns] = standard_scaler.fit_transform(features[continue_columns])

# 给数据插入一列全为1的偏置项权重
features['bias'] = 1

# 再处理分类的数据，one-hot编码
classes_columns = ['make', 'fuel-type', 'aspiration', 'num-of-doors',
                   'body-style', 'drive-wheels', 'engine-location',
                   'engine-type', 'num-of-cylinders', 'fuel-system']
dummies = pd.get_dummies(features[classes_columns])
features = features.join(dummies)
features.drop(classes_columns,axis=1,inplace=True)
features.to_csv(os.path.join(os.getcwd(),'Datas','Data-Cleaning-2.csv'),index=False)
