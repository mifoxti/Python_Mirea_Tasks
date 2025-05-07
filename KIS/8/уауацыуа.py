def main(value):
    int_value = int(value)
    c1 = (int_value >> 0) & 0b11
    c2 = (int_value >> 2) & 0b111
    c3 = (int_value >> 5) & 0b000000
    c4 = (int_value >> 11) & 0b111111111
    c5 = (int_value >> 20) & 0b111111111
    return {'T1': str(int(c1)), 'T2': str(int(c2)),
            'T4': str(int(c4)), 'T5': str(int(c5))}


print(main(287965218))
