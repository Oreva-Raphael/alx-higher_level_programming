#!/usr/bin/python3
def no_c(my_string):
    l_string =  list(my_string)
    new_list = [char for char in l_string if char != 'c' and char != 'C']
    my_string = ''.join(new_list)
    return my_string
