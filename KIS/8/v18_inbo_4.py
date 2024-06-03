def main(value):
    int_value = int(value, 16)
    G1 = (int_value >> 0) & 0b1
    G2 = (int_value >> 1) & 0b1111
    G3 = (int_value >> 5) & 0b11
    G4 = (int_value >> 7) & 0b1111111111
    G5 = (int_value >> 17) & 0b111
    return {'G1': str(int(G1)), 'G2': str(int(G2)), 'G3': str(int(G3)),
            'G4': str(int(G4)), 'G5': str(int(G5))}


print(main("0x33920"))