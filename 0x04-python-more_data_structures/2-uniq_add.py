#!/usr/bin/python3
def uniq_add(my_list=[]):
    lists = []
    for i in my_list:
        if i not in lists:
            lists.append(i)
    sum = 0
    for j in lists:
        sum += j
    return sum
