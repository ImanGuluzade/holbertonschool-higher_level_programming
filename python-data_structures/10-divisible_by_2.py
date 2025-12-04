#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Return a list of True/False depending on whether each element
    in my_list is divisible by 2."""
    result = []
    for num in my_list:
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
