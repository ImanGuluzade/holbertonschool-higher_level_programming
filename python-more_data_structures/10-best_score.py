#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value"""
    if not a_dictionary or len(a_dictionary) == 0:
        return None
    best_key = max(a_dictionary, key=lambda k: a_dictionary[k])
    return best_key
