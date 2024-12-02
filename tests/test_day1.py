from day1 import DayOne
from unittest import TestCase

class TestDayOne(TestCase):

    def test_day_1_part_1(self):
        test_dayone = DayOne()
        expected_result = 11
        result = test_dayone.handler("test_input_part_1.txt")
        self.assertEqual(expected_result, result)


    def test_day_1_part_2(self):
        test_dayone = DayOne()
        expected_result = 31
        result = test_dayone.part2_handler("test_input_part_1.txt")
        self.assertEqual(expected_result, result)