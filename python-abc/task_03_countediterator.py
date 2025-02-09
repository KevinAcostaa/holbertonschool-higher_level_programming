#!/usr/bin/python3


class CountedIterator:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.count = 0

    def get_count(self):
        return self.count

    def __next__(self):
        valor = next(self.iterable)
        self.count += 1

        return  valor
