#!/usr/bin/python3
""" Defines a function"""


def class_to_json(obj):
    """ Function that retuns the dictionary description of an obj """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
