#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        mirror = my_list.copy()
        return mirror
    else:
        mirror = my_list.copy()
        mirror.pop(idx)
        mirror.insert(idx, element)
        return mirror
