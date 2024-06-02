def main(hex_string):
    int_value = int(hex_string, 10)
    x1 = (int_value >> 0) & 0b1111111111
    x3 = (int_value >> 16) & 0b111111111
    x4 = (int_value >> 25) & 0b11111111111
    return hex(x1), hex(x3), hex(x4)


# Тестируем функцию с примерами
print(main('27320729867'))
print(main('23302452124'))
print(main('1354721528'))
print(main('31602564737'))
