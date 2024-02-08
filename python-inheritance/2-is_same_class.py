#!/usr/bin/python3
"""Defines a class """


def is_same_class(obj, a_class):
    """returns True if the object is an instance."""
    if type(obj) == a_class:
        return True
    return False
