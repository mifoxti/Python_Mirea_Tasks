def main(data):
    my_dict = {}
    for name in data:
        value = name[1]
        v = int(value, 16)
        my_dict[name[0]] = v
    V1 = bin(int(my_dict['V1']))[2:].zfill(2)
    V2 = bin(int(my_dict['V2']))[2:].zfill(7)
    V3 = bin(int(my_dict['V3']))[2:].zfill(8)
    V4 = bin(int(my_dict['V4']))[2:].zfill(2)
    return int(V4 + V3 + V2 + V1, 2)


print(main([('V1', '0x1'), ('V2', '0xd'), ('V3', '0x97'), ('V4', '0x1')]))
print(main([('V1', '0x1'), ('V2', '0x7a'), ('V3', '0xf5'), ('V4', '0x2')]))
print(main([('V1', '0x0'), ('V2', '0xf'), ('V3', '0x76'), ('V4', '0x0')]))
print(main([('V1', '0x1'), ('V2', '0x7d'), ('V3', '0x68'), ('V4', '0x0')]))
