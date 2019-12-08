#!/usr/bin/python3
# -*- coding: utf-8 -*-
from unittest import main, TestCase

from src.day4 import Solver


class SolverTest(TestCase):
    """
    Test case for day 2
    """

    def setUp(self):
        self.s = Solver()

    def test_password_length(self):
        params = [
            (1, False),
            (-1, False),
            (10000, False),
            (55555555555555555555555, False),
            (111111, True)
        ]
        for value, expect in params:
            with self.subTest(value=value, expect=expect):
                self.assertEqual(self.s.match_password_length(value), expect)

    def test_password_is_in_range(self):
        params = [
            (100000, 100000, 100000, True),
            (100000, 200000, 300000, False),
            (-100000, 100000, 000000, True),
            (-100000, 100000, -200000, False),
            (1, 2, 3, False)
        ]
        for start, end, value, expect in params:
            with self.subTest(start=start, end=end, value=value, expect=expect):
                self.s.start = start
                self.s.end = end
                self.assertEqual(self.s.in_range(value), expect)

    def test_password_adjacent_digits(self):
        params = [
            (112233, True),
            (123456, False),
            (-312344, True),
            (-165654, False),
        ]
        for value, expect in params:
            with self.subTest(value=value, expect=expect):
                self.assertEqual(self.s.has_adjacent_number(value), expect)

    def test_password_decrease_number(self):
        params = [
            (223345, False),
            (123456, False),
            (-102323, True)
        ]
        for value, expect in params:
            with self.subTest(value=value, expect=expect):
                self.assertEqual(self.s.has_decrease_number(value), expect)

    def test_password_is_valid(self):
        params = [
            (111111, True),
            (223450, False),
            (123789, False)
        ]
        for value, expect in params:
            with self.subTest(value=value, expect=expect):
                self.assertEqual(self.s.is_valid(value), expect)


if __name__ == '__main__':
    main()
