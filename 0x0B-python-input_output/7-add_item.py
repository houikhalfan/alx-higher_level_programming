#!/usr/bin/python3
"""Module that loads, adds and saves arguments to a Python list"""
from sys import argv


p_load_file = __import__('6-load_from_json_file').load_from_json_file
file_save = __import__('5-save_to_json_file').save_to_json_file

try:
    json_list = p_load_file('add_item.json')
except (ValueError, FileNotFoundError):
    json_list = []

for item in argv[1:]:
    json_list.append(item)

file_save(json_list, 'add_item.json')
