#!/usr/bin/python3
def print_last_digit(number):
    num = int(str(number)[-1])
    print("{}".format(num), end="")
    return num
