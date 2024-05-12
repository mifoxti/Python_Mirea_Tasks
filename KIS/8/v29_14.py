def main(hex_string):
    int_value = int(hex_string, 16)
    f1 = (int_value >> 0) & 0b111111111
    f2 = (int_value >> 9) & 0b1111
    f3 = (int_value >> 13) & 0b111
    f4 = (int_value >> 16) & 0b1111
    f5 = (int_value >> 20) & 0b0000
    d1 = bin(f1)[2:].zfill(9)
    d2 = bin(f2)[2:].zfill(4)
    d3 = bin(f3)[2:].zfill(3)
    d4 = bin(f4)[2:].zfill(4)
    d5 = bin(f5)[2:].zfill(4)

    result = [
        ("F1", str(int(d1, 2))),
        ("F2", str(int(d2, 2))),
        ("F3", str(int(d3, 2))),
        ("F4", str(int(d4, 2))),
    ]
    return result


# Пример использования
hex_string = "0xfdd19"
result_array = main(hex_string)
print(result_array)  # [('F1', '281'), ('F2', '14'), ('F3', '6'), ('F4', '15')]
