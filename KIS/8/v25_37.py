def main(data):
    my_dict = {}
    for name, value in data:
        v = value
        my_dict[name] = v
    u1 = bin(int(my_dict['U1']))[2:].zfill(9)
    u2 = bin(int(my_dict['U2']))[2:].zfill(1)
    u3 = bin(int(my_dict['U3']))[2:].zfill(4)
    u4 = bin(int(0))[2:].zfill(1)
    u5 = bin(int(my_dict['U5']))[2:].zfill(8)
    u6 = bin(int(my_dict['U6']))[2:].zfill(4)

    return str(hex(int(u6 + u5 + u4 + u3 + u2 + u1, 2)))


print(main([('U1', 31), ('U2', 0), ('U3', 7), ('U5', 189), ('U6', 5)]))
