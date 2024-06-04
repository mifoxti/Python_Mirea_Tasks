def main(hex_string):
    int_value = int(hex_string)
    J1 = (int_value >> 0) & 0b11111111
    J2 = (int_value >> 8) & 0b11
    J3 = (int_value >> 10) & 0b111111111
    J4 = (int_value >> 19) & 0b1111
    J5 = (int_value >> 23) & 0b111111
    J1 = bin(J1)[2:].zfill(8)
    J2 = bin(J2)[2:].zfill(2)
    J3 = bin(J3)[2:].zfill(9)
    J4 = bin(J4)[2:].zfill(4)
    J5 = bin(J5)[2:].zfill(6)
    result = [
        ("J1", str(hex(int(J1, 2)))),
        ("J2", str(hex(int(J2, 2)))),
        ("J3", str(hex(int(J3, 2)))),
        ("J4", str(hex(int(J4, 2)))),
        ("J5", str(hex(int(J5, 2)))),
    ]
    return result


# Пример использования
hex_string = "239942723"
result_array = main(hex_string)
print(result_array)  # [('F1', '281'), ('F2', '14'), ('F3', '6'), ('F4', '15')]
