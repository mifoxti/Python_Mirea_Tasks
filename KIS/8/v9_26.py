def main(value):
    int_value = int(value)
    p1 = (int_value >> 0) & 0b111111111
    p2 = (int_value >> 9) & 0b111111
    p3 = (int_value >> 15) & 0b11
    p4 = (int_value >> 17) & 0b1111111111
    p5 = (int_value >> 27) & 0b00000000
    p6 = (int_value >> 35) & 0b1
    return {'P1': str(int(p1)), 'P2': str(int(p2)), 'P3': str(int(p3)),
            'P4': str(int(p4)), 'P6': str(int(p6))}


print(main("55616642357"))