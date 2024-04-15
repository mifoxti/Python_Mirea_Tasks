def main(data):
    my_dict = {}
    for name, value in data:
        v = int(value, 16)
        my_dict[name] = v
    d1 = bin(int(my_dict['O1']))[2:].zfill(8)
    d2 = bin(int(my_dict['O2']))[2:].zfill(4)
    d3 = bin(int(my_dict['O3']))[2:].zfill(8)
    d4 = bin(int(my_dict['O4']))[2:].zfill(6)
    return str(int(d4 + d3 + d2 + d1, 2))


print(main([('O1', '0x70'), ('O2', '0x7'), ('O3', '0x12'), ('O4', '0x26')]))  # '39921520'
# print(main([('O1', '0xc'), ('O2', '0xe'), ('O3', '0x79'), ('O4', '0x1f')]))   # '33005068'
# print(main([('O1', '0x2c'), ('O2', '0xb'), ('O3', '0x2a'), ('O4', '0x8')]))    # '8563500'
# print(main([('O1', '0x57'), ('O2', '0x4'), ('O3', '0x17'), ('O4', '0x2')]))     # '2192471'
