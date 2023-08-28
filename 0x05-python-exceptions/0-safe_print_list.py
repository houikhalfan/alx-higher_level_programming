#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        c = 0
        for i in my_list:
            if c < x:
                print(i, end='')
                c += 1
        print()
    except IndexError:
        pass
    return (c)
