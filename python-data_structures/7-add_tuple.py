#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure each tuple has at least 2 elements, filling with 0 if needed
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    print(tuple_a)
    print(tuple_b)
    # Create a new tuple with the sum of corresponding elements
    result_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return result_tuple
