def main(data):
    my_dict = {}
    for name, value in data:
        v = value
        my_dict[name] = v
    N1 = bin(int(my_dict['N1']))[2:].zfill(7)
    N2 = bin(int(my_dict['N2']))[2:].zfill(10)
    N3 = bin(int(my_dict['N3']))[2:].zfill(4)
    N4 = bin(int(my_dict['N4']))[2:].zfill(9)
    N5 = bin(int(my_dict['N5']))[2:].zfill(3)
    N6 = bin(int(my_dict['N6']))[2:].zfill(9)
    return hex(int(N6 + N5 + N4 + N3 + N2 + N1, 2))


print(main([('N1', '123'), ('N2', '575'), ('N3', '10'), ('N4', '291'), ('N5', '2'), ('N6', '177')]))
