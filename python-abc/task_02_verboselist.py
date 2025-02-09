#!/usr/bin/python3


from typing import Iterable


class VerboseList(list):
    def append(self, element):
        super().append(element)
        print("Added [{}] to the list.".format(element))

    def extend(self, items):
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, delete):
        super().remove(delete)
        print("Removed [{}] from the list.".format(delete))

    def pop(self, index: int = - 1):
        items = super().pop(index)
        print("Popped [{}] from the list.".format(items))
        return items
