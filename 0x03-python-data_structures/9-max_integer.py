#!/usr/bin/python3
def len_(my_list):
    output = 0
    for q in my_list:
        output += 1
    return output

def max_integer(my_list=[]):
    if len_(my_list) == 0:
        return None
    else:
        greatest = my_list[0]
        for w in my_list:
            if isinstance(w, (int, float)):
                if w > greatest:
                    greatest = w
            else:
                continue
        return greatest
