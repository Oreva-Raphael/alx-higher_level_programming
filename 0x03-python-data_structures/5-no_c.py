#!/usr/bin/python3
def no_c(my_string):
    l_string =  list(my_string)
    for w in range(len(l_string) -1, -1, -1):
        if l_string[w] == 'c' or l_string[w] == 'C':
            l_string.pop(w)
    my_string = ''.join(l_string)
    return my_string
