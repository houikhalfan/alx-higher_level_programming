#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = set_2.difference(set_1)
    set_4 = set_1.difference(set_2)
    set_4.update(set_3)
    return set_4
