import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import missingno as msno


data = pd.read_csv(os.path.join(os.getcwd(), 'Datas', 'sh600621.csv'))
print(data.head())

