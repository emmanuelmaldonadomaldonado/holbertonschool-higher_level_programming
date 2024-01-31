#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Create parapeters

        Args:
            size (int): the size
        """
        if not isinstance(self, size=0):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Check for area"""
        return self.__size * self.__size
