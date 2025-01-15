#!/usr/bin/python3
inicio = ord('a')
final = ord('z')
for i in range(inicio, final + 1):
    if i == 101 or i == 113:
        i = i + 1
    else:
        print("{:c}".format(i), end="")
