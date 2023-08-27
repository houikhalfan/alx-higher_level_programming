#!/usr/bin/python3
def islower(c):
    ascii_value = ord(c)
    return ascii_value >= 97 and ascii_value <= 122

# Test cases
print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))
