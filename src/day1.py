#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from math import floor


class SolverError(RuntimeError):
    pass


class Solver:

    def __init__(self):
        self.sum = 0
        self.file = None

    def open(self, file):
        self.file = open(file, "r")

    def solve(self, number) -> int:
        if type(number) != int:
            raise SolverError("'" + number + "' is not a number")
        res = floor(number / 3) - 2
        self.sum += res
        return res

    def process(self):
        for line in self.file:
            self.solve(int(line))
        return self.sum


if __name__ == '__main__':
    s = Solver()
    s.open(os.path.dirname(os.path.realpath(__file__)) + "/../inputs/day1.txt")
    print(s.process())
