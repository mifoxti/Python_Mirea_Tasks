def main(data):
    my_dict = {}
    for name in data.keys():
        value = data[name]
        v = int(value)
        my_dict[name] = v
    L1 = bin(int(my_dict['L1']))[2:].zfill(10)
    L2 = bin(0)[2:].zfill(8)
    L3 = bin(int(my_dict['L3']))[2:].zfill(2)
    L4 = bin(int(my_dict['L4']))[2:].zfill(6)
    L5 = bin(int(my_dict['L5']))[2:].zfill(6)
    L6 = bin(int(my_dict['L6']))[2:].zfill(1)
    return int(L6 + L5 + L4 + L3 + L2 + L1, 2)


print(main({'L1': '243', 'L3': '3', 'L4': '0', 'L5': '51', 'L6': '91'}))
