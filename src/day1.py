#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from math import floor


class SolverError(RuntimeError):
    pass


class Solver:

    def __init__(self):
        self.sum = 0

    def solve(self, number) -> int:
        if type(number) != int:
            raise SolverError("'" + number + "' is not a number")
        return floor(number / 3) - 2

    def solve_recursive(self, number):
        if type(number) != int:
            raise SolverError("'" + number + "' is not a number")
        res = floor(number / 3) - 2
        if res <= 0:
            return 0
        return res + self.solve_recursive(res)

    def process(self, filename: str):
        self.sum = 0
        with open(filename, "r") as file:
            for line in file:
                self.sum += self.solve(int(line))
        return self.sum

    def process_recursive(self, filename: str):
        self.sum = 0
        with open(filename, "r") as file:
            for line in file:
                self.sum += self.solve_recursive(int(line))
        return self.sum


if __name__ == '__main__':
    s = Solver()
    f = os.path.dirname(os.path.realpath(__file__)) + "/../inputs/day1.txt"
    print(f'Solve simple : {s.process(f)}')
    print(f'Solve recursion : {s.process_recursive(f)}')
