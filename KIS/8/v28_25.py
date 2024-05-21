def main(hex_string):
    int_value = int(hex_string, 16)
    v1 = (int_value >> 0) & 0b1
    v2 = (int_value >> 1) & 0b11111111
    v3 = (int_value >> 9) & 0b1111111
    v4 = (int_value >> 16) & 0b111111111
    v5 = (int_value >> 25) & 0b1111111
    return {'V1': str(hex(v1)), 'V3': str(hex(v3)),
            'V4': str(hex(v4)), 'V5': str(hex(v5))}


print(main('0x6797ca22'))