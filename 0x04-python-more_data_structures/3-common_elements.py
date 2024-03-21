#!/usr/bin/python3
def common_elements(set_1, set_2):
    newSet = set()
    # return (set_1.intersection(set_2))
    for w in set_2:
        for p in set_1:
            if w == p:
                newSet.add(i)
    return newSet
