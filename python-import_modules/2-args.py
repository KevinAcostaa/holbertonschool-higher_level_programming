#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    arguments = len(argv[1:])
    if arguments == 1:
        print("{} argument:".format(arguments))
    elif arguments != 0:
        print("{} arguments:".format(arguments))
    else:
        print("{} arguments.".format(arguments))
    for i, arg in enumerate(argv[1:], start=1):
        print("{}: {}".format(i, arg))