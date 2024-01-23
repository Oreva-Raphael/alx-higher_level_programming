#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = ()
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    max_tuple = (len_a) if (len(tuple_a) > len(tuple_b)) else (len_b)
    for x in range(2):
        if (x < len_a) and (x < len_b):
            result += (tuple_a[x] + tuple_b[x]),
        elif x >= len_a:
            result += (tuple_b[x]),
        elif x >= len_b:
            result += (tuple_a[x]),
    return result
