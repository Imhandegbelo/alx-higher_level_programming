#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x intgers of a list.
    Args:
        my_list: The list to print elements from.
        x (int): The number of elements of my_list to print.
    Returns:
        The number of elements printed.
    """
    return_val = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            return_val += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (return_val)
