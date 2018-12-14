import pandas as pd
import six
from abc import ABCMeta

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

    def __init__(self, decorated_data_frame, specific_date, from_time, to_time):
        AbstractDataFrameDecorator.__init__(self, decorated_data_frame)
        self.specific_date = specific_date
        self.from_time = from_time
        self.to_time = to_time

    def filter(self):
        global decorated_df
        self.decorated_data_frame.filter()
        date_time1 = pd.to_datetime(self.specific_date + ' ' + self.from_time)
        date_time2 = pd.to_datetime(self.specific_date + ' ' + self.to_time)
        print("time:", date_time1, date_time2)
        print(decorated_df.time.dt.date, date_time1.date(), "dates@!!!!")
        print(len(decorated_df), "*********0*********")

        decorated_df = decorated_df[decorated_df.time.dt.date == date_time1.date()]
        print(len(decorated_df), "*********1*********")
        decorated_df = decorated_df[
            (decorated_df.time.dt.time >= date_time1.time()) & (decorated_df.time.dt.time <= date_time2.time())]
        print(len(decorated_df), "********2**********")

    def get_filter_name(self):
        print('Filter by date and time')
        return 'Filter by date and time'


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
            start_time = argument_dictionary[arg]['start_time']
            end_time = argument_dictionary[arg]['end_time']
            concrete_data_frame = FilterByDateAndTime(concrete_data_frame, date, start_time, end_time)

        if arg == 'location_filter':
            print(argument_dictionary[arg])
            p1_x = int(argument_dictionary[arg]['x1'])
            p1_y = int(argument_dictionary[arg]['y1'])

            p2_x = int(argument_dictionary[arg]['x2'])
            p2_y = int(argument_dictionary[arg]['y2'])
            print("coordiantes:", p1_x, p1_y, p2_x, p2_y)
            concrete_data_frame = FilterByLocation(concrete_data_frame, (p1_x, p1_y), (p2_x, p2_y))
            print(len(decorated_df))
    concrete_data_frame.filter()
    print(len(decorated_df))
    return decorated_df
