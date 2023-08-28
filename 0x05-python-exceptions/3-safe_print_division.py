#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        di = (a / b)
    except ZeroDivisionError:
        di = None
    finally:
        print("Inside result: {}".format(di))
        return (di)
