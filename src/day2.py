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
        print(sublist, sublist[0])
        return [sublist[0]] if sublist[0] == 99 and len(sublist) >= 1 else sublist

    def handle_sublist(self, sublist: list):
        if type(sublist) != list or len(sublist) != 4:
            raise SolverError("Need 4 item in a list to process")
        operation, index1, index2, res_index = sublist
        if operation == 99:
            return None
        res = self.items[index1] + self.items[index2] if operation == 1 else self.items[index1] * self.items[index2]
        self.items[res_index] = res
        return res

    def handle_find_item(self, sublist: list, seek: int):
        print(sublist)
        if type(sublist) != list or len(sublist) != 4:
            raise SolverError("Need 4 item in a list to process")
        operation, noun, verb, res_index = sublist

        if operation == 99:
            return None
        return self.items[noun] + self.items[verb] if operation == 1 else self.items[noun] * self.items[verb]

    def find_item(self, filename: str, seek: int = 19690720):
        with open(filename, "r") as file:
            line = file.read()
            self.items = list(map(lambda x: int(x), line.split(',')))
            i = 0
            sublist = self.get_sublist(4, i)
            res = self.handle_find_item(sublist, seek)
            while res != seek:
                sublist = self.get_sublist(4, i)
                i += len(sublist)
                res = self.handle_find_item(sublist, seek)
                print(res)
        return sublist[1], sublist[2]

    def process(self, filename: str):
        with open(filename, "r") as file:
            line = file.read()
            self.items = list(map(lambda x: int(x), line.split(',')))
            i = 0
            while self.handle_sublist(self.get_sublist(4, i)) is not None:
                i += 4
        return self.items[0]


if __name__ == '__main__':
    s = Solver()
    f = os.path.dirname(os.path.realpath(__file__)) + "/../inputs/day2.txt"
    print(f'Solve simple : {s.process(f)}')
    print(f'Solve find item : {s.find_item(f, 19690720)}')
