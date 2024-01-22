def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0 ,0)

    first_tuple = (tuple_a[0] + tuple_b[0])
    second_tuple = (tuple_a[1] + tuple_b[1])
    return(first_tuple, second_tuple)
