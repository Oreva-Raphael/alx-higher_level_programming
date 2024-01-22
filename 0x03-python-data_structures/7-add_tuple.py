def add_tuple(tuple_a=(), tuple_b=()):
    result = ()
    len_a = len(tuple_a)
    len__b = len(tuple_b)

    max_length = max(len_a, len__b)
    
    for i in range(2):
        if i < len_a and i < len__b:
            result += (tuple_a[i] + tuple_b[i]),
        elif i >= len_a:
            result += (tuple_b[i]),
        elif i >= len__b:
            result += (tuple_a[i]),
    
    return result
