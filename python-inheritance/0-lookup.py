#!/usr/bin/python3
"""Defines an object"""


def lookup(obj):
   """Returns a list of available attributes and methods of an object"""
   list = dir(obj) 
   return list
