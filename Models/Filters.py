import pandas as pd
import six
from abc import ABCMeta
from settings import df_by_obj

main_df = pd.read_pickle('../data/paths.pkl.xz')
decorated_df = main_df
print(len(main_df), "say my name!")


@six.add_metaclass(ABCMeta)
class AbstractDataFrame:

    def filter(self):
        pass

    def get_filter_name(self):
        pass


class ConcreteDataFrame(AbstractDataFrame):
    def __init__(self):
        global decorated_df
        global main_df
        decorated_df = main_df

    def filter(self):
        pass

    def get_filter_name(self):
        return 'Concrete Filter'

    def get_data_frame(self):
        return decorated_df


@six.add_metaclass(ABCMeta)
class AbstractDataFrameDecorator(AbstractDataFrame):

    def __init__(self, decorated_data_frame):
        self.decorated_data_frame = decorated_data_frame

    def filter(self):
        return self.decorated_data_frame.filter()

    def get_data_frame(self):
        return decorated_df

    def get_filter_name(self):
        return "**" + self.decorated_data_frame.get_filter_name() + "**"


class FilterByDateAndTime(AbstractDataFrameDecorator):

    def __init__(self, decorated_data_frame, specific_date):
        AbstractDataFrameDecorator.__init__(self, decorated_data_frame)
        self.specific_date = specific_date

    def filter(self):
        global decorated_df
        self.decorated_data_frame.filter()
        date_time1 = pd.to_datetime(self.specific_date)
        date_time2 = pd.to_datetime(self.specific_date)
        print(len(decorated_df), "*********0*********")
        decorated_df = decorated_df[decorated_df.time.dt.date == date_time1.date()]
        print(len(decorated_df), "*********1*********")

    def get_filter_name(self):
        print('Filter by date')
        return 'Filter by date'


class FilterByTime(AbstractDataFrameDecorator):

    def __init__(self, decorated_data_frame, from_time, to_time):
        AbstractDataFrameDecorator.__init__(self, decorated_data_frame)
        self.to_time = to_time
        self.from_time = from_time

    def filter(self):
        global decorated_df
        self.decorated_data_frame.filter()
        date_time1 = pd.to_datetime(self.from_time)
        date_time2 = pd.to_datetime(self.to_time)
        decorated_df = decorated_df[
            (decorated_df.time.dt.time >= date_time1.time()) & (decorated_df.time.dt.time <= date_time2.time())]

    def get_filter_name(self):
        print("Filter by time")
        return "Filter by time"


class FilterByLocation(AbstractDataFrameDecorator):

    def __init__(self, decorated_data_frame, coordinate1, coordinate2):
        print("Filter by location constructor1")
        AbstractDataFrameDecorator.__init__(self, decorated_data_frame)
        print("Filter by location constructor2")
        self.x1, self.y1 = coordinate1
        self.x2, self.y2 = coordinate2
        print("Filter by location constructor3")

    def filter(self):
        global decorated_df
        self.decorated_data_frame.filter()
        decorated_df = decorated_df[
            ((decorated_df.x >= self.x1) & (decorated_df.x <= self.x2))
            & ((decorated_df.y >= self.y1) & (
                    decorated_df.y <= self.y2))]
        print(len(decorated_df), "length of decorated_df")

    def get_filter_name(self):
        print('Filter by location')
        return 'Filter by location'


class FilterByMultiLocation(AbstractDataFrameDecorator):
    def __init__(self, decorated_data_frame, set_of_coordinate):
        print("Filter by multi location constructor1")
        AbstractDataFrameDecorator.__init__(self, decorated_data_frame)
        print("Filter by multi location constructor2")
        self.set_of_coordinate = set_of_coordinate
        print("Filter by multi location constructor3")

    def filter(self):
        global decorated_df
        indexes = set()
        self.decorated_data_frame.filter()
        print("ARE YOU GETTING HERE!")
        for coordinate in self.set_of_coordinate:
            print("ARE YOU ?!")
            print(coordinate, type(coordinate[0]))
            tmp_df = decorated_df
            print(len(decorated_df))
            tmp_df = tmp_df[((tmp_df.x >= coordinate[0]) & (tmp_df.x <= coordinate[2])) & (
                    (tmp_df.y >= coordinate[1]) & (tmp_df.y <= coordinate[3]))]
            objs = tmp_df.groupby(['filename', 'objectNum']).size()
            print(objs)

            for t, n in objs.iteritems():
                print(t)
                indexes.add(t)
        print("ARE YOU GETTING HERE(2)!")
        print(indexes, "Indexes")
        objs_list = list(indexes)

        print(objs_list)
        if len(objs_list) > 0:
            decorated_df = df_by_obj.loc[objs_list]
        else:
            decorated_df = []

    def get_filter_name(self):
        print('Filter by multi location')
        return 'Filter by multi location'


def arguments_receiver_and_filter(argument_dictionary):
    print("im' here")
    concrete_data_frame = ConcreteDataFrame()
    for arg in argument_dictionary.keys():
        print(arg)
        if arg == 'time_filter':
            start_time = argument_dictionary[arg]['start_time']
            print("start time: ", start_time)
            end_time = argument_dictionary[arg]['end_time']
            print("end time:", end_time)
            concrete_data_frame = FilterByTime(concrete_data_frame, start_time, end_time)

        if arg == 'date_filter':
            date = argument_dictionary[arg]['date']
            concrete_data_frame = FilterByDateAndTime(concrete_data_frame, date)

        if arg == 'location_filter':
            print(argument_dictionary[arg])
            p1_x = int(argument_dictionary[arg]['x1'])
            p1_y = int(argument_dictionary[arg]['y1'])
            p2_x = int(argument_dictionary[arg]['x2'])
            p2_y = int(argument_dictionary[arg]['y2'])
            print("coordiantes:", p1_x, p1_y, p2_x, p2_y)
            concrete_data_frame = FilterByLocation(concrete_data_frame, (p1_x, p1_y), (p2_x, p2_y))
            print(len(decorated_df))
        if arg == 'multi_location_filter':
            print(argument_dictionary[arg]['set_of_coordinates'], "*********************")
            concrete_data_frame = FilterByMultiLocation(concrete_data_frame,
                                                        argument_dictionary[arg]['set_of_coordinates'])
            print("TTTTTTTTTTTTT")

    concrete_data_frame.filter()
    print(len(decorated_df))
    return decorated_df
