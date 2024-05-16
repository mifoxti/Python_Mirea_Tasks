def main(data):
    my_dict = {}
    for name in data:
        value = data[name]
        v = int(value, 16)
        my_dict[name] = v
    d1 = bin(int(my_dict['O1']))[2:].zfill(6)
    d2 = bin(int(0))[2:].zfill(7)
    d3 = bin(int(my_dict['O3']))[2:].zfill(8)
    d4 = bin(int(my_dict['O4']))[2:].zfill(9)
    d5 = bin(int(my_dict['O5']))[2:].zfill(6)
    return str(int(d5 + d4 + d3 + d2 + d1, 2))


print(main({'O1': '0x3f', 'O3': '0xf0', 'O4': '0x50', 'O5': '0x22'}))
