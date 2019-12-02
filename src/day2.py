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

    def process(self, first_item=None, second_item=None):
        i = 0
        self.items[1] = first_item if first_item is not None else self.items[1]
        self.items[2] = second_item if second_item is not None else self.items[2]
        while self.handle_sublist(self.get_sublist(4, i)) is not None:
            i += 4
        return self.items[0]

    def find(self, seek):
        final_noun = final_verb = None
        backup = self.items.copy()
        for noun in range(100):
            for verb in range(100):
                self.items = backup.copy()
                output = self.process(noun, verb)
                if output == seek:
                    final_noun = noun
                    final_verb = verb
                    break
            if final_verb is not None and final_noun is not None:
                break
        return final_noun, final_verb

    def init(self, filename: str):
        with open(filename, "r") as file:
            line = file.read()
            self.items = list(map(lambda x: int(x), line.split(",")))


if __name__ == '__main__':
    s = Solver()
    f = os.path.dirname(os.path.realpath(__file__)) + "/../inputs/day2.txt"
    s.init(f)
    print(f'Solve simple : {s.process(12, 2)}')
    s.init(f)
    res_noun, res_verb = s.find(19690720)
    print(f'Solve find item : {100 * res_noun + res_verb}')
