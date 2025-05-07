def main(value):
    int_value = int(value)
    G1 = (int_value >> 0) & 0b11
    G2 = (int_value >> 2) & 0b111111111
    G3 = (int_value >> 11) & 0b111111
    G4 = (int_value >> 17) & 0b1111111
    G5 = (int_value >> 24) & 0b111111
    return [
        ("A1", int(G1)),
        ("A2", int(G2)),
        ("A3", int(G3)),
        ("A4", int(G4)),
        ("A5", int(G5)),
    ]


print(main("556155184"))
