def main(value):
    int_value = int(value, 16)
    l1 = (int_value >> 0) & 0b1111
    l2 = (int_value >> 4) & 0b1111111111
    l3 = (int_value >> 14) & 0b1
    l4 = (int_value >> 15) & 0b11111
    l5 = (int_value >> 20) & 0b1111111
    l6 = (int_value >> 27) & 0b1111111
    return {'L1': int(l1), 'L2': int(l2), 'L3': int(l3),
            'L4': int(l4), 'L5': int(l5), 'L6': int(l6)}


print(main('0x1d84a0cb1'))
