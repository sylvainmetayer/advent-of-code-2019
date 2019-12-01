#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from unittest import main, TestCase

from src.day1 import Solver, SolverError


class SolverTest(TestCase):
    """
    Test case for day 1
    """

    def setUp(self):
        self.s = Solver()

    def test_day1(self):
        self.assertEqual(0, self.s.sum)
        self.assertIsNone(self.s.file)

    def test_open_file(self):
        self.s.open(os.path.dirname(os.path.realpath(__file__)) + "/../inputs/day1.txt")
        self.assertIsNotNone(self.s.file)

    def test_open_file_fail(self):
        with self.assertRaises(FileNotFoundError):
            self.s.open("inputs/day1.txt")

    def test_simple_solver(self):
        self.assertEqual(2, self.s.solve(12))

    def test_edge_case_solver(self):
        self.assertEqual(2, self.s.solve(14))

    def test_case_solver(self):
        self.assertEqual(33583, self.s.solve(100756))

    def test_solver_sum(self):
        self.s.solve(12)
        self.s.solve(12)
        self.assertEqual(4, self.s.sum)

    def test_solve_bad_value(self):
        with self.assertRaises(SolverError):
            self.s.solve("test")


if __name__ == '__main__':
    main()
