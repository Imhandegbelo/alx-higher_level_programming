#!/usr/bin/python3
"""
function to replace an element in a list
"""

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    length = len(my_list)
    if idx > length - 1:
        return my_list
    my_list[idx] = element
    return my_list
