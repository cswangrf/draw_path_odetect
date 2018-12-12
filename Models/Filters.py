from pylab import *
from matplotlib import pyplot as plt
import pandas as pd


class Filter:


    def __init__(self):
        print("start filter")
        self.bg = imread("../paths0.png")
        self.df = pd.read_pickle('../data/paths.pkl.xz')

    def locate_time(self, start_time, end_time):

        x = start_time.split(':')
        y = end_time.split(':')
        dh = self.df[self.df.time.dt.hour.between(int(x[0]), int(y[0]))]
        dd = dh[dh.time.dt.minute.between(int(x[1]), int(y[1]))]
        objs = dd.groupby(['filename', 'objectNum']).size()
        df_by_obj = dd.set_index(['filename', 'objectNum']).sort_index()
        imshow(self.bg, alpha=0.5)
        for t, n in objs.iteritems():
            o = df_by_obj.loc[t]
            plt.plot(o.x, o.y)
        plt.show()

    def locate_date(self, date, s_time, e_time):
        x = s_time.split(':')
        y = e_time.split(':')
        dates = pd.to_datetime(date)
        d_d = self.df[self.df.time.dt.date == dates.date()]
        dh = d_d[d_d.time.dt.hour.between(int(x[0]), int(y[0]))]
        dd = dh[dh.time.dt.minute.between(int(x[1]), int(y[1]))]
        objs = dd.groupby(['filename', 'objectNum']).size()
        df_by_obj = dd.set_index(['filename', 'objectNum']).sort_index()
        imshow(self.bg, alpha=0.5)
        for t, n in objs.iteritems():
            o = df_by_obj.loc[t]
            plt.plot(o.x, o.y)
        plt.show()

    # def seq_locat(self, x, y, size):
    #     location1 = [x + n for n in range(size)]
    #     locatiion2= [y + n for n in range(size)]
    #     d_d = df[df.]




# x.locat_time('13:12','13:12') #test filter by time
# x.locat_date('2017-08-17','11:00','15:15') # test filter by date and time