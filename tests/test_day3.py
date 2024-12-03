from unittest import TestCase
from day3 import DayThree

class DayOneTests(TestCase):

    def test_day_3_part_1(self):
        test_day3 = DayThree()
        result = test_day3.handler("test_input_day3_p1.txt")
        self.assertEqual(161, result)
