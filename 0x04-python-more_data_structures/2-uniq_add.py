#!/usr/bin/python3
def uniq_add(my_list=[]):
    order = set(my_list)
    new_list = list(order)
    sum = 0
    for w in range(len(new_list)):
        sum += new_list[w]
    return sum
