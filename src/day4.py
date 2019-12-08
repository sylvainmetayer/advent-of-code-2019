#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Solver:

    def __init__(self, start: int = 0, end: int = 0, password_length: int = 6):
        self._start = start
        self._end = end
        self.password_length = password_length

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value

    def match_password_length(self, value):
        return len(str(value)) == self.password_length

    def in_range(self, value):
        return self.start <= value <= self.end

    def has_adjacent_number(self, value):
        current = None
        for char in str(value):
            if current == char:
                return True
            current = char
        return False

    def has_decrease_number(self, value):
        array_value = list(str(value).replace("-", ""))
        for i, number in enumerate(array_value):
            if len(array_value) > i + 1 and number > array_value[i + 1]:
                return True
        return False

    def is_valid(self, value):
        return self.match_password_length(value) and \
               self.has_adjacent_number(value) and not self.has_decrease_number(value)

    def solve(self):
        valid_password_count = 0
        for i in range(self.start, self.end):
            if self.in_range(i) and self.is_valid(i):
                valid_password_count += 1
        return valid_password_count


if __name__ == '__main__':
    s = Solver(356261, 846303)
    print(f"{s.solve()} valid passwords within range")
