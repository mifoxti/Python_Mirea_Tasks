def main(data):
    my_dict = {}
    for name in data.keys():
        value = data[name]
        v = int(value)
        my_dict[name] = v
    L1 = bin(int(my_dict['L1']))[2:].zfill(5)
    L2 = bin(int(my_dict['L2']))[2:].zfill(1)
    L3 = bin(int(my_dict['L3']))[2:].zfill(10)
    L4 = bin(int(my_dict['L4']))[2:].zfill(9)
    L5 = bin(int(my_dict['L5']))[2:].zfill(10)
    L6 = bin(int(my_dict['L6']))[2:].zfill(9)
    return str(hex(int(L6 + L5 + L4 + L3 + L2 + L1, 2)))


print(main({'L1': 20, 'L2': 1, 'L3': 524, 'L4': 46, 'L5': 712, 'L6': 137}))
