import unittest

from day_2.A_report_checker import get_level_difference, is_report_safe

class TestReportChecker(unittest.TestCase):
    def test_get_level_difference_returns_zero_when_both_values_are_equal(self):
        self.assertEqual(get_level_difference(1, 1), 0)

    def test_get_level_difference_returns_one_when_values_have_a_difference_of_one(self):
        self.assertEqual(get_level_difference(1, 2), 1)

    def test_get_level_difference_returns_three_when_values_are_three_apart(self):
        self.assertEqual(get_level_difference(1, 4), 3)

    def test_get_level_difference_works_when_a_negative_number_is_supplied(self):
        self.assertEqual(get_level_difference(1, -1), 2)

    def test_is_report_safe_returns_true_when_all_values_are_increasing_by_one(self):
        self.assertTrue(is_report_safe([1,2,3,4,5]))

    def test_is_report_safe_returns_true_when_all_values_are_increasing_by_two(self):
        self.assertTrue(is_report_safe([1,3,5,7,9]))

    def test_is_report_safe_returns_true_when_all_values_are_increasing_by_three(self):
        self.assertTrue(is_report_safe([1,4,7,10,13]))

    def test_is_report_safe_returns_false_when_all_values_are_increasing_but_one_pair_by_four(self):
        self.assertFalse(is_report_safe([1,4,7,10,14]))

    def test_is_report_safe_returns_false_when_two_consecutive_values_are_the_same(self):
        self.assertFalse(is_report_safe([1,1,4,7,10]))

    def test_is_report_safe_returns_false_when_all_values_are_decreasing_but_one_pair_by_four(self):
        self.assertFalse(is_report_safe([14,10,7,4,1]))

    def test_is_report_safe_returns_true_when_all_values_are_decreasing_by_three(self):
        self.assertTrue(is_report_safe([13,10,7,4,1]))

    def test_is_report_safe_returns_true_when_all_values_are_decreasing_by_two(self):
        self.assertTrue(is_report_safe([9,7,5,3,1]))

    def test_is_report_safe_returns_true_when_all_values_are_decreasing_by_one(self):
        self.assertTrue(is_report_safe([5,4,3,2,1]))

    def test_is_report_safe_returns_false_when_all_values_are_increasing_except_one_pair(self):
        self.assertFalse(is_report_safe([1,2,1,2,3]))

    def test_is_report_safe_returns_false_when_all_values_are_decreasing_except_one_pair(self):
        self.assertFalse(is_report_safe([5,4,5,4,3]))

if __name__ == '__main__':
    unittest.main()
