#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value is None:
        return a_dictionary
    keys_to_delete = []
    for k, v in a_dictionary.items():
        if v == value:
            keys_to_delete.append(k)
    for i in keys_to_delete:
        del a_dictionary[i]
    return a_dictionary
