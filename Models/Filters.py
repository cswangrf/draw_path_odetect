import pandas as pd
import six
from abc import ABCMeta

main_df = pd.read_pickle('../data/paths.pkl.xz')
decorated_df = main_df
print(len(main_df))


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
        decorated_df = decorated_df[decorated_df.time.dt.date == date_time1.date()]
        decorated_df = decorated_df[
            (decorated_df.time.dt.time >= date_time1.time()) & (decorated_df.time.dt.time <= date_time2.time())]

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
        AbstractDataFrameDecorator.__init__(self, decorated_data_frame)
        self.x1, self.y1 = coordinate1
        self.x2, self.y2 = coordinate2

    def filter(self):
        global decorated_df
        self.decorated_data_frame.filter()
        decorated_df = decorated_df[
            ((decorated_df.x >= self.x1) & (decorated_df.x <= self.x2))
            & ((decorated_df.y >= self.y1) & (
                    decorated_df.y <= self.y2))]

    def get_filter_name(self):
        print('Filter by location')
        return 'Filter by location'


def arguments_receiver_and_filter(argument_dictionary):

    concrete_data_frame = ConcreteDataFrame()
    for arg in argument_dictionary.keys():
        if arg == 'time_filter':
            start_time = argument_dictionary[arg]['start_time']
            print(start_time)
            end_time = argument_dictionary[arg]['end_time']
            print(end_time)
            FilterByTime(concrete_data_frame, start_time, end_time)

        if arg == 'date_filter':
            date = argument_dictionary[arg]['date']
            start_time = argument_dictionary[arg]['start_time']
            end_time = argument_dictionary[arg]['end_time']
            FilterByDateAndTime(concrete_data_frame, date, start_time, end_time)

        if arg == 'location_filter':
            p1_x = argument_dictionary[arg]['x1']
            p1_y = argument_dictionary[arg]['y1']

            p2_x = argument_dictionary[arg]['x2']
            p2_y = argument_dictionary[arg]['y2']

            FilterByLocation(concrete_data_frame, tuple(p1_x, p1_y), tuple(p2_x, p2_y))
    concrete_data_frame.filter()