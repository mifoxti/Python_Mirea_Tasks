def main(data):
    my_dict = {}
    for name, value in data:
        v = value
        my_dict[name] = v
    F1 = bin(int(my_dict['F1']))[2:].zfill(2)
    F2 = bin(int(my_dict['F2']))[2:].zfill(8)
    F3 = bin(int(my_dict['F3']))[2:].zfill(6)
    F4 = bin(int(my_dict['F4']))[2:].zfill(4)
    F5 = bin(int(my_dict['F5']))[2:].zfill(4)
    F6 = bin(int(my_dict['F6']))[2:].zfill(8)
    return int(F6 + F5 + F4 + F3 + F2 + F1, 2)


print(main([('F1', 0), ('F2', 247), ('F3', 50), ('F4', 4), ('F5', 5), ('F6', 44)]))
print(main([('F1', 0), ('F2', 104), ('F3', 53), ('F4', 15), ('F5', 2), ('F6', 58)]))
print(main([('F1', 0), ('F2', 112), ('F3', 42), ('F4', 13), ('F5', 8), ('F6', 172)]))