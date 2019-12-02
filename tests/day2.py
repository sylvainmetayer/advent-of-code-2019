#!/usr/bin/python3
# -*- coding: utf-8 -*-
from unittest import main, TestCase

from src.day2 import Solver, SolverError


class SolverTest(TestCase):
    """
    Test case for day 2
    """

    def setUp(self):
        self.s = Solver()

    def test_sublist(self):
        self.s.items = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        self.assertEqual([1, 9, 10, 3], self.s.get_sublist())

    def test_sublist_middle(self):
        self.s.items = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        self.assertEqual([2, 3, 11, 0], self.s.get_sublist(4, 4))

    def test_sublist_end(self):
        self.s.items = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        self.assertEqual([99, 30, 40, 50], self.s.get_sublist(4, 8))

    def test_sublist_more_than_end(self):
        self.s.items = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        self.assertEqual([99, 30, 40, 50], self.s.get_sublist(5, 8))

    def test_handle_sublist_without_4_items(self):
        with self.assertRaises(SolverError):
            self.s.items = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
            self.s.handle_sublist([1, 2])

    def test_handle_sublist_addition(self):
        self.s.items = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        self.s.handle_sublist([1, 9, 10, 3])
        self.assertEqual(70, self.s.items[3])

    def test_handle_sublist_multiply(self):
        self.s.items = [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        self.s.handle_sublist([2, 3, 11, 0])
        self.assertEqual(3500, self.s.items[0])

    def test_handle_sublist_halt(self):
        self.s.items = [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        self.assertIsNone(self.s.handle_sublist([99, 30, 40, 50]))

    def test_handle_sublist_without_list(self):
        with self.assertRaises(SolverError):
            self.s.items = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
            self.s.handle_sublist(1)


if __name__ == '__main__':
    main()
