def main(data):
    my_dict = {}
    for name in data:
        value = data[name]
        v = int(value, 16)
        my_dict[name] = v
    L1 = bin(int(my_dict['L1']))[2:].zfill(2)
    L2 = bin(int(my_dict['L2']))[2:].zfill(6)
    L3 = bin(int(my_dict['L3']))[2:].zfill(1)
    L4 = bin(int(my_dict['L4']))[2:].zfill(8)
    L5 = bin(int(my_dict['L5']))[2:].zfill(5)
    return str(hex(int(L5 + L4 + L3 + L2 + L1, 2)))


print(main({'L1': '0x3', 'L2': '0x33', 'L3': '0x0', 'L4': '0x61', 'L5': '0x6'}))
