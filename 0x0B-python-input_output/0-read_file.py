#!/usr/bin/python3
"""This module creates a funtion that reads a text file and prints it"""


def read_file(filename=""):
    """opens and reads a file"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
