#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """class with pbc attribut"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """if i got no attribute every thing will be retrived
        but if there is name contained only the name will be retrived"""
        if attrs is None:
            return self.__dict__
        rs = {}
        for attr in attrs:
            if hasattr(self, attr):
                value = getattr(self, attr)
                rs[attr] = value
        return rs
