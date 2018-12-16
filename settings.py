import pandas as pd
from matplotlib import pyplot as plt
from pylab import *
df = pd.read_pickle('../data/paths.pkl.xz')
df_by_obj = df.set_index(['filename', 'objectNum']).sort_index()
set_of_coordinates = set()


class image:
    def __init__(self, path):
        self.bg = imread(path)
        self.image_height, self.image_width, self.z = self.bg.shape

    def set_img(self, im_path ):
        self.bg = imread(im_path)
        self.image_height, self.image_width, self.z = self.bg.shape


im = image("../paths0.png")
