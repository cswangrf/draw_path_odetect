from pylab import *
from matplotlib import pyplot as plt
import pandas as pd


class Filter:
    def __init__(self):
        print("start filter")
        self.bg = imread("../paths0.png")
        self.df = pd.read_pickle('../data/paths.pkl.xz')

    def located_time(self, s_time, e_time):
        x = s_time.split(':')
        y = e_time.split(':')
        dh = self.df[self.df.time.dt.hour.between(int(x[0]), int(y[0]))]
        dd = dh[dh.time.dt.minute.between(int(x[1]), int(y[1]))]
        objs = dd.groupby(['filename', 'objectNum']).size()
        df_by_obj = dd.set_index(['filename', 'objectNum']).sort_index()
        return self.plots(objs, df_by_obj)

    def located_date(self, date, s_time, e_time,df):
        x = s_time.split(':')
        y = e_time.split(':')
        dates = pd.to_datetime(date)
        d_d = df[df.time.dt.date == dates.date()]
        dh = d_d[d_d.time.dt.hour.between(int(x[0]), int(y[0]))]
        dd = dh[dh.time.dt.minute.between(int(x[1]), int(y[1]))]
        objs = dd.groupby(['filename', 'objectNum']).size()
        df_by_obj = dd.set_index(['filename', 'objectNum']).sort_index()
        return self.plots(objs, df_by_obj)

    def sequence_location(self, x, y, x1, y1):
        dd = self.df[((self.df.x >= x) & (self.df.x <= x1)) & ((self.df.y >= y) & (self.df.y <= y1))]
        objs = dd.groupby(['filename', 'objectNum']).size()
        objs = objs.sample(15)
        df_by_obj = self.df.set_index(['filename', 'objectNum']).sort_index()
        return self.plots(objs, df_by_obj)

    def plots(self, objs, df_by_obj):
        imshow(self.bg, alpha=0.5)
        for t, n in objs.iteritems():
            o = df_by_obj.loc[t]
            plt.plot(o.x, o.y)
        return plt
