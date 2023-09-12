#!/usr/bin/python3
"""Adds all arguments to a python list"""
import sys
import json
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


file_name = "add_item.json"
data_list = []

if path.exists(file_name):
    data_list = load_from_json_file(file_name)

for arg in sys.argv[1:]:
    data_list.append(arg)

save_to_json_file(data_list, file_name)
