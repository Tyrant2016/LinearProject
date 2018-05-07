import pandas as pd
import numpy as np
from statsmodels.distributions.empirical_distribution import ECDF
import matplotlib.pyplot as plt
import seaborn as sns

# plt.plot([1,2,3,1],[1,2,3,4])
# plt.show()
# ecdf = ECDF([1,2,3,4,5,6,7])
# print(ecdf.x)
# print(ecdf.y)
# print(ecdf([1,1,1,1]))
a1 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9],
                   [1, 2, 3], [4, 5, 6], [7, 8, 9]],
                  columns=['A', 'B', 'C'])
# print(a1)
# # print(np.tri(5,5,k=0))
# print('-----------------------------------')
# print(np.tri(3,3,k=-1).T)
# print('-----------------------------------')
# a2 = pd.DataFrame([[1,2,7],
#                   [4,5,2],
#                   [3,8,9]])
# print(a2)
# print(111111111111111111)
# print(*a2)
# print(a2.shape)
# print(*a2.shape)
# print(111111111111111)
# print(a2*np.tri(*a2.shape,k=-1).T)
# print(np.tri(5,5,k=1))
# g1 = a1.groupby(['A','B'])
# for i in g1:
#     print(i)
# print(a1)
# print('-----------------------------------')
# print(a1[a1.A == 4])
# print('-----------------------------------')
# print(a1[a1.A == 4]['A'])
# print('-----------------------------------')
# a1.loc[a1.A == 4, 'A'] = 100
# print(a1)
# print('-----------------------------------')
# g1 = a1.groupby('A')
# for name,value in g1:
#     print('name:{}'.format(name))
#     print('value:\n{}'.format(value))
#     print('**************')
# g2 = g1.A
# for x in g2:
#     print(x[0])
#     print('=========')
#     print(x[1])
#     print('*********')

# a2 = a1.loc[a1.A==100].copy()
# print(a2)
# a2.loc[1,'B']=77
# print(a2)
a3 = pd.DataFrame([[1, 2],
                   [3, 4]])

a4 = pd.DataFrame([[0, 1],
                   [0, 0]])

a5 = pd.DataFrame([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])


# print(a3*a4)
# print(a3.mul(a4))
# print(np.tri(*a3.values.shape,k=-1).T)
# print(a3.stack())
# print(a3.stack().abs())
# print(a3.reindex([1,0]))
# t1 = np.triu_indices(1, 3)
def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
    plt.show()

sinplot()
sns.set()
sinplot()
print('This is a test999')

