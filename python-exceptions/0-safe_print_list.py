#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    countX = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            countX += 1
    except IndexError:
        pass
    finally:
        print()
        return countX
