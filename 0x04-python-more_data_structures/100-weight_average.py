#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    add = 0
    divisor = 0
    for top_score in my_list:
        add += (top_score[0] * top_score[1])
        divisor += top_score[1]
    return add / divisor
