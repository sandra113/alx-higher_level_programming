def safe_print_list_integers(my_list=[], x=0):
    num_elements = 0
    i = 0

    while num_elements < x:
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end='')
                num_elements += 1
            i += 1
        except IndexError:
            break
    print()
    return num_elements
