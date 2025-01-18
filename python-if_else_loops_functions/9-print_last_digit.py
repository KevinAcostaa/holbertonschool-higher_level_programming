 #!/usr/bin/python3
def print_last_digit(number):
     last_num = str(number)
     last_num = last_num[-1]
     number = int(last_num)
     print("{0}".format(number), end='')
     return number