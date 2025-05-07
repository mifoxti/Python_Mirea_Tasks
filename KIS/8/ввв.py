def main(value):
    int_value = int(value, 16)
    G1 = (int_value >> 0) & 0b11111
    G2 = (int_value >> 5) & 0b1111
    G3 = (int_value >> 9) & 0b111
    G4 = (int_value >> 12) & 0b11111111
    return G1, G2, G3, G4


print(main("0x85261"))
