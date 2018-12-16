import Models.Filters as solveit

import unittest


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.caps_df = solveit.ConcreteDataFrame()

    def test_read_file(self):
        self.assertNotEqual(len(self.caps_df.get_data_frame()), 0)

    def test_one_filter_time(self):
        self.caps_df = solveit.FilterByTime(self.caps_df, "13:00:00", "13:10:00")
        self.caps_df.filter()
        self.assertEqual(len(self.caps_df.get_data_frame()), 24238)

    def test_multi_filter_time(self):
        self.caps_df = solveit.FilterByTime(self.caps_df, "13:00:00", "13:10:00")
        self.caps_df = solveit.FilterByTime(self.caps_df, "13:00:00", "13:05:00")
        self.caps_df.filter()
        self.assertEqual(len(self.caps_df.get_data_frame()), 8081)

    def test_location(self):
        self.caps_df = solveit.FilterByLocation(self.caps_df, (12, 12), (50, 50))
        self.caps_df.filter()
        self.assertEqual(len(self.caps_df.get_data_frame()), 1337)

    def test_time_then_location(self):
        self.caps_df = solveit.FilterByTime(self.caps_df, "13:00:00", "13:10:00")
        self.caps_df = solveit.FilterByTime(self.caps_df, "13:00:00", "13:05:00")
        self.caps_df = solveit.FilterByLocation(self.caps_df, (12, 12), (50, 50))
        self.caps_df.filter()
        self.assertEqual(len(self.caps_df.get_data_frame()), 32)

    def test_time_and_location(self):
        self.caps_df = solveit.FilterByDateAndTime(self.caps_df, "2017-08-17")
        self.caps_df = solveit.FilterByTime(self.caps_df, "10:00:00", "17:05:00")
        self.caps_df.filter()
        self.assertEqual(len(self.caps_df.get_data_frame()), 136881)

    def test_multi_location(self):
        self.caps_df=solveit.FilterByMultiLocation(self.caps_df,((0,0,20,20),(50,50,60,60)))
        self.caps_df.filter()
        self.assertEqual(len(self.caps_df.get_data_frame()), 1114)

if __name__ == '__main__':
    unittest.main()
