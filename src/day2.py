#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os


class SolverError(RuntimeError):
    pass


class Solver:

    def __init__(self):
        self.items = list()

    def get_sublist(self, number: int = 4, offset: int = 0) -> list:
        return self.items[offset: offset + number]

    def handle_sublist(self, sublist: list):
        if type(sublist) != list or len(sublist) != 4:
            raise SolverError("Need 4 item in a list to process")
        operation, index1, index2, res_index = sublist
        if operation == 99:
            return None
        res = self.items[index1] + self.items[index2] if operation == 1 else self.items[index1] * self.items[index2]
        self.items[res_index] = res
        return res

    def process(self, filename: str):
        with open(filename, "r") as file:
            i = 0
            line = file.read()
            self.items = list(map(lambda x: int(x), line.split(',')))
            print(self.items)
            i = 0
            while self.handle_sublist(self.get_sublist(4, i)) is not None:
                i += 4
        return self.items


if __name__ == '__main__':
    s = Solver()
    f = os.path.dirname(os.path.realpath(__file__)) + "/../inputs/day2.txt"
    print(f'Solve simple : {s.process(f)}')
