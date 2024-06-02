def main(data):
    my_dict = {}
    for name in data.keys():
        value = data[name]
        v = int(value)
        my_dict[name] = v
    Y1 = bin(int(my_dict['Y1']))[2:].zfill(4)
    Y2 = bin(0)[2:].zfill(9)
    Y3 = bin(int(my_dict['Y3']))[2:].zfill(9)
    Y4 = bin(int(my_dict['Y4']))[2:].zfill(10)
    return int(Y4 + Y3 + Y2 + Y1, 2)


print(main({'Y1': '11', 'Y3': '216', 'Y4': '845'}))
