import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import time

cost = list()
times = 1000000


def gradient_descent(rate, theta, x_train, y_train):
    m = 1 / x_train.shape[0]  # 这是训练数据的数量要除的那个,我先把他化成1/m
    gradient = theta.copy()
    for index, theta_i in enumerate(theta):
        gradient[index] = rate * m * (x_train.dot(theta).sub(y_train, axis=0).T.dot(x_train.iloc[:, index]))
    theta -= gradient
    return theta


def cost_function(x_train, y_train, theta):
    m = 1 / (x_train.shape[0] * 2)
    cost = m * (((x_train.dot(theta).sub(y_train, axis=0)) ** 2).sum(axis=0))
    print(cost)
    return cost


data = pd.read_csv(os.path.join(os.getcwd(), 'Datas', 'Data-Cleaning-2.csv'))

continue_columns = ['symboling', 'normalized-losses', 'volume',
                    'horsepower', 'bore', 'stroke', 'compression-ratio',
                    'peak-rpm', 'highway-mpg', 'engine-size']
new_continue2 = data[continue_columns] ** 2
new_continue2.columns = ['symboling2', 'normalized-losses2', 'volume2',
                         'horsepower2', 'bore2', 'stroke2', 'compression-ratio2',
                         'peak-rpm2', 'highway-mpg2', 'engine-size2']
data = data.join(new_continue2)
new_continue3 = data[continue_columns] ** 3
new_continue3.columns = ['symboling3', 'normalized-losses3', 'volume3',
                         'horsepower3', 'bore3', 'stroke3', 'compression-ratio3',
                         'peak-rpm3', 'highway-mpg3', 'engine-size3']
data = data.join(new_continue3)

target = data['price']
features = data.drop('price', axis=1)
seed = 123
x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=seed)
theta = np.ones((features.shape[1], 1))

start_time = time.time()
while times:
    theta = gradient_descent(0.001, theta, x_train, y_train)
    cost.append(cost_function(x_train, y_train, theta))
    times -= 1
print('cost', cost[len(cost) - 1], 'times:', time.time() - start_time)
