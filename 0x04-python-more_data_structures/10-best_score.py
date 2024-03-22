#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    benchmark = 0
    max_key = None

    for key, value in a_dictionary.items():
        if value is None:
            return None
        elif value > benchmark:
            benchmark = value
            max_key = key
    return max_key
