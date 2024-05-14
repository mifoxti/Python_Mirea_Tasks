def main(hex_string):
    int_value = int(hex_string, 16)
    f1 = (int_value >> 0) & 0b1111111
    f2 = (int_value >> 7) & 0b1111
    f3 = (int_value >> 11) & 0b111
    f4 = (int_value >> 14) & 0b1111111111
    f5 = (int_value >> 24) & 0b111
    f6 = (int_value >> 27) & 0b11111
    result = ((f5 << 29) | (f6 << 24) | (f2 << 20)
              | (f1 << 13) | (f4 << 3) | f3)
    return str(int(result))


print(main('0x2d769f9e'))