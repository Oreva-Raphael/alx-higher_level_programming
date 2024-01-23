#!/usr/bin/python3

def delete_at(mylist=[], idx=0):
    list_length = len(mylist)
    if (idx < 0) | (idx >= list_length):
        return mylist
    w = 0
    while w <= idx:
        if w == idx:
            mylist.remove(mylist[w])
        w += 1
    return mylist
