import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

# read the file
df_x = pd.read_table('logistic_x.txt', sep='\s+', header=None)
df_y = pd.read_table('logistic_y.txt', header=None)

# change the columns' names
df_x.rename(columns={0 : 'x1', 1 : 'x2'}, inplace=True)
df_x['x0'] = 1 
df_x = df_x[['x0', 'x1', 'x2']]
df_y.rename(columns={0 : 'y1'}, inplace=True)

