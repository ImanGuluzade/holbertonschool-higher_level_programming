#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides two integers and prints the result.

    Returns the result of division, or None if division cannot be performed.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
