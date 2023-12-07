#!/usr/bin/python3
'''
function that replaces all occurences of an element by another in a new list
@my_list: the list
@search: the element to search for 
@replace: the new element
'''


def search_replace(my_list, search, replace):
    if my_list:
        new_list = my_list.copy()
        length = len(new_list) - 1
        for i in range(length):
            if new_list[i] == search:
                new_list[i] = replace
        return new_list
