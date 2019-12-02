#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os


class SolverError(RuntimeError):
    pass


class Solver:

    def __init__(self):
        self.items = list()

    def get_sublist(self, number: int = 4, offset: int = 0) -> list:
        sublist = self.items[offset: offset + number]
        return [sublist[0]] if len(sublist) >= 1 and sublist[0] == 99 else sublist

    def handle_sublist(self, sublist: list):
        if type(sublist) != list:
            raise SolverError("Need a list to process")
        if len(sublist) == 1 and sublist[0] == 99:
            return None
        if len(sublist) != 4:
            raise SolverError("Need 4 items to process")
        operation, index1, index2, res_index = sublist
        res = self.items[index1] + self.items[index2] if operation == 1 else self.items[index1] * self.items[index2]
        self.items[res_index] = res
        return res

    def handle_find_item(self, sublist: list, seek: int):
        if type(sublist) != list:
            raise SolverError("Need a list to process")
        if len(sublist) == 1 and sublist[0] == 99:
            return None
        if len(sublist) != 4:
            print(sublist)
            raise SolverError("test")
        operation, noun, verb, res_index = sublist

        if not 0 <= noun <= 99 or not 0 <= verb <= 99:
            self.items[res_index] = self.items[noun] + self.items[verb] \
                if operation == 1 else self.items[noun] * self.items[verb]

        print(f'operation {operation} : noun({noun}): {self.items[noun]} - '
              f'verb({verb}): {self.items[verb]} - res({res_index}):{self.items[res_index]}')

        return self.items[res_index]

    def find_item(self, seek: int):
        backup = self.items.copy()
        i = 0
        sublist = self.get_sublist(4, i)
        res = self.handle_find_item(sublist, seek)
        while res != seek:
            sublist = self.get_sublist(4, i)
            i += len(sublist) if len(sublist) > 0 else 1
            res = self.handle_find_item(sublist, seek)
            if res is None:
                self.items = backup
            print(f'i = {i} : {sublist} => "{res}"')
        if len(sublist) == 2:
            return sublist[1], sublist[2]
        return None

    def process(self):
        i = 0
        while self.handle_sublist(self.get_sublist(4, i)) is not None:
            i += 4
        return self.items[0]

    def init(self, filename: str):
        with open(filename, "r") as file:
            line = file.read()
            self.items = list(map(lambda x: int(x), line.split(",")))


if __name__ == '__main__':
    s = Solver()
    f = os.path.dirname(os.path.realpath(__file__)) + "/../inputs/day2.txt"
    s.init(f)
    print(f'Solve simple : {s.process()}')
    s.init(f)
    print(f'Solve find item : {s.find_item(19690720)}')
