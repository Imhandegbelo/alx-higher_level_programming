#!/usr/bin/python3
"""Defines a class Base"""
import json
import os
import csv
import turtle


class Base:
    """Represents the base with a private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
