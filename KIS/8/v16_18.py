def main(data):
    my_dict = {}
    for name in data.keys():
        value = data[name]
        v = int(value)
        my_dict[name] = v
    V1 = bin(int(my_dict['I1']))[2:].zfill(1)
    V2 = bin(int(my_dict['I2']))[2:].zfill(9)
    V3 = bin(int(my_dict['I3']))[2:].zfill(9)
    V4 = bin(int(my_dict['I4']))[2:].zfill(6)
    return str(int(V4 + V3 + V2 + V1, 2))


main({'I1': '1', 'I2': '147', 'I3': '97', 'I4': '19'})

main({'I1': '1', 'I2': '69', 'I3': '82', 'I4': '17'})

main({'I1': '1', 'I2': '298', 'I3': '335', 'I4': '15'})

main({'I1': '0', 'I2': '252', 'I3': '386', 'I4': '29'})
