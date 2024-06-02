def main(value):
    int_value = int(value)
    c1 = (int_value >> 0) & 0b11111
    c2 = (int_value >> 5) & 0b1111
    c3 = (int_value >> 9) & 0b111111
    c4 = (int_value >> 15) & 0b111111
    c5 = (int_value >> 21) & 0b11111111
    return {'C1': int(c1), 'C2': int(c2), 'C3': int(c3),
            'C4': int(c4), 'C5': int(c5)}


print(main(94626633))