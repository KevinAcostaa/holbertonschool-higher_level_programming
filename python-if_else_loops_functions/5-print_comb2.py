#!/usr/bin/python3
numbers = ["{:02}".format(i) for i in range(0, 99)]
print(", ".join(numbers))
