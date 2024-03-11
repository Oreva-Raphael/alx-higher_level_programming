#!/usr/bin/python3
def no_c(my_string):
    string_without = ""
    for char in (my_string):
        if (char != 'c') & (char != 'C'):
            string_without += char
    return string_without
