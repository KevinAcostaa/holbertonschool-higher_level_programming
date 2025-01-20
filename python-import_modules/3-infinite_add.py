#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    i = 0
    for arg in argv[:]:
        i += int(arg)
        print(i)
