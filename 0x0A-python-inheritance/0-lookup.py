#!/usr/bin/python3
"""An object attribute lookup function."""

def lookup(obj):
    """Returns a list of availale attributes and methods of an object"""
    return dir(obj)
