#!/usr/bin/python3
""" Define a function """
import json


def load_from_json_file(filename):
    """ Function that returns an object by a JSON representation

    Args:
        my_str: JSON representation

    Raises:
        Exception: when the string can't be decoded

    """
    with open(filename, 'w', encoding="utf-8") as f:
        return json.loads(f)
