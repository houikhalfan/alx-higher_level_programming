#!/usr/bin/python3
def safe_print_integer(value):
    try:
        forma = "{:d}".format(value)
        print(forma)
        return True
    except:
        return False
