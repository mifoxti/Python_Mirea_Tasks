def main(hex_string):
    int_value = int(hex_string, 16)
    x1 = (int_value >> 0) & 0b0000000000
    x2 = (int_value >> 10) & 0b11111
    x3 = (int_value >> 15) & 0b111111
    x4 = (int_value >> 21) & 0b111111
    x5 = (int_value >> 27) & 0b1111111111
    x6 = (int_value >> 37) & 0b111
    x1 = bin(x1)[2:].zfill(10)
    x2 = bin(x2)[2:].zfill(5)
    x3 = bin(x3)[2:].zfill(6)
    x4 = bin(x4)[2:].zfill(6)
    x5 = bin(x5)[2:].zfill(10)
    x6 = bin(x6)[2:].zfill(3)

    result = [
        ("X2", str(int(x2, 2))),
        ("X3", str(int(x3, 2))),
        ("X4", str(int(x4, 2))),
        ("X5", str(int(x5, 2))),
        ("X6", str(int(x6, 2))),
    ]
    return result


# Пример использования
hex_string = "0x475c8e3de"
result_array = main(hex_string)
print(result_array)  # [('F1', '281'), ('F2', '14'), ('F3', '6'), ('F4', '15')]
