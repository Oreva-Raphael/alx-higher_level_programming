#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for w in range(len(new_list)):
        if new_list[w] == search:
            new_list.pop(w)
            new_list.insert(w, replace)
    return new_list
