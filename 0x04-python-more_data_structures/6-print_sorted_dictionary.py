#!/usr/bin/python3
'''
function that prints a dictinary by ordered keys
'''


def print_sorted_dictionary(a_dictionary):
    sorted_dict = dict(sorted(a_dictionary.items()))
    print(sorted_dict)
