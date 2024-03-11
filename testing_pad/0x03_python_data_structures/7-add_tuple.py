#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len__b = len(tuple_b)
    result = ()
    idx = 0

    if (len_a < 2):
        len_a = 2 - len_a
        for i in range(len_a):
            tuple_a += 0,
    if (len__b < 2):
        len__b = 2 - len__b
        for i in range(len__b):
            tuple_b += 0,
    while idx < 2:
        result += ((tuple_a[idx] + tuple_b[idx]), )
        idx += 1
    return (result)
