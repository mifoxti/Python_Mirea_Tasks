def main(value):
    int_value = int(value)
    B1 = str((int_value >> 0) & 0b11111111)
    B2 = str((int_value >> 8) & 0b11111)
    B3 = str((int_value >> 13) & 0b111)
    B4 = str((int_value >> 16) & 0b111)
    B5 = str((int_value >> 19) & 0b111111)
    B6 = str((int_value >> 25) & 0b111111111)
    return (B1, B2, B3, B4, B5, B6)
