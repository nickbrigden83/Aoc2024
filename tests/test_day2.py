from unittest import TestCase
from day2 import DayTwo

class DayTwoTests(TestCase):

    def test_part_one(self):
        test_day_two = DayTwo()
        result = test_day_two.part1_handler("test_input_day_2.txt")
        print(result)