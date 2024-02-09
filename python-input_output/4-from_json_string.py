#!/usr/bin/python3
"""Define a function"""


import json

def from_json_string(my_str):
    """ Function that returns the JSON representation of an object

    Args:
        my_obj: object

    Raises:
        Exception: when the object can't be encoded

    """
    return json.loads(my_str)
