import pandas as pd
from matplotlib import pyplot as plt
from pylab import *

bg = imread("../paths0.png")
df = pd.read_pickle('../data/paths.pkl.xz')
df_by_obj = df.set_index(['filename', 'objectNum']).sort_index()

t = bg.shape
x = t[1]
y = t[0]
di = {}
counter = 0
for x1 in range(0,x,int(x/10)):
    for y1 in range(0, y, int(y / 10)):
        di[counter]=[0+x1,0+y1,x1+x/10,y1+y/10]
        counter+=1