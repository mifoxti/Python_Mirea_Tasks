def main(data):
    my_dict = {}
    for name, value in data:
        v = int(value, 16)
        my_dict[name] = v
    C1 = bin(int(my_dict['C1']))[2:].zfill(6)
    C2 = bin(int(my_dict['C2']))[2:].zfill(2)
    C3 = bin(int(my_dict['C3']))[2:].zfill(3)
    C4 = bin(0)[2:].zfill(4)
    C5 = bin(int(my_dict['C5']))[2:].zfill(7)
    C6 = bin(int(my_dict['C6']))[2:].zfill(10)
    return str(int(C6 + C5 + C4 + C3 + C2 + C1, 2))


print(main([('C1', '0xc'), ('C2', '0x3'), ('C3', '0x0'), ('C5', '0x2f'), ('C6', '0x23f')]))
print(main([('C1', '0x2'), ('C2', '0x3'), ('C3', '0x6'), ('C5', '0x2a'), ('C6', '0x173')]))
print(main([('C1', '0x1d'), ('C2', '0x1'), ('C3', '0x6'), ('C5', '0x51'), ('C6', '0x3cc')]))
print(main([('C1', '0x38'), ('C2', '0x0'), ('C3', '0x1'), ('C5', '0x60'), ('C6', '0x165')]))
