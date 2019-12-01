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

    def test_simple_solver(self):
        self.assertEqual(2, self.s.solve(12))

    def test_edge_case_solver(self):
        self.assertEqual(2, self.s.solve(14))

    def test_case_solver(self):
        self.assertEqual(33583, self.s.solve(100756))

    def test_solver_sum(self):
        self.s.sum += self.s.solve(12)
        self.s.sum += self.s.solve(12)
        self.assertEqual(4, self.s.sum)

    def test_solve_bad_value(self):
        with self.assertRaises(SolverError):
            self.s.solve("test")

    def test_solver_recursive(self):
        self.assertEqual(2, self.s.solve_recursive(14))

    def test_solver_recursive_edge_case(self):
        self.assertEqual(966, self.s.solve_recursive(1969))

    def test_solver_recursive_sum(self):
        self.s.sum += self.s.solve_recursive(1969)
        self.assertEqual(966, self.s.sum)

    def test_process_solve(self):
        f = os.path.dirname(os.path.realpath(__file__)) + "/../inputs/day1.txt"
        self.assertEqual(3363033, self.s.process(f))

    def test_process_solve_recursive(self):
        f = os.path.dirname(os.path.realpath(__file__)) + "/../inputs/day1.txt"
        self.assertEqual(3363033, self.s.process(f))


if __name__ == '__main__':
    main()
