import pandas as pd
from matplotlib import pyplot as plt
from pylab import *

bg = imread("../paths0.png")
df = pd.read_pickle('../data/paths.pkl.xz')
df_by_obj = df.set_index(['filename', 'objectNum']).sort_index()
set_of_coordinates = set()
image_height,image_width,z= bg.shape

