def max_integer(my_list=[]):
    if not my_list:
        return None
    
    greatest = my_list[0]
    for w in my_list:
        if w > greatest:
            greatest = w
    return greatest
