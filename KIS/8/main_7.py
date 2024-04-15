def main(hex_str):
    int_value = int(hex_str, 16)

    P1 = (int_value >> 0) & 0b111
    P2 = (int_value >> 3) & 0b111111
    P3 = (int_value >> 9) & 0b11111111
    P4 = (int_value >> 17) & 0b111

    result = (P3 << 12) + (P1 << 9) + (P4 << 6) + (P2 << 0)

    return result

print(main('0x75d37'))
print(main('0x39aa9'))
print(main('0x29dd4'))
