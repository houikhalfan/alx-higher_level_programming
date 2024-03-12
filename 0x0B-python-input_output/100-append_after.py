#!/usr/bin/python3
"""Module that contains the function append_after"""


def append_after(file_name="", p_search_tring="", p_new_string=""):
    """function that inserts a line of text to a file, after each line,
    containing a specific string.

    Args:
        filename (str, optional): name of file. Defaults to "".
        search_string (str, optional): string to search. Defaults to "".
        new_string (str, optional): string to append. Defaults to "".
    """
    with open(file_name, "r") as f:
        text = f.readlines()

    with open(file_name, "w") as fo:
        s = ""
        for line in text:
            s += line
            if p_search_tring in line:
                s += p_new_string
        fo.write(s)
