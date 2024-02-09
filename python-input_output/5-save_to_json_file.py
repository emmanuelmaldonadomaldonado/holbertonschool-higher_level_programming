#!/usr/bin/python3
""" Define a function """
import json


def save_to_json_file(my_obj, filename):
    """ Function that returns an object by a JSON representation

    Args:
        my_str: JSON representation

    Raises:
        Exception: when the string can't be decoded

    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
