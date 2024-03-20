#!/usr/bin/python3
#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list.copy()
    if idx >= len(my_list):
        return my_list.copy()
    else:
        copy_list = list(my_list)
        copy_list[idx] = element
        return copy_list
