def main(data):
    data = int(data)

    d1 = data & 0b111
    d2 = (data & 0b0) >> 3
    d3 = (data & 0b111111000000000) >> 9
    d4 = (data & 0b111111111000000000000000) >> 15

    hex_str = hex((d2 << 18) | (d1 << 15) | (d3 << 9) | d4)

    return hex_str

# Тестовые примеры
print(main(6123525))  # '0x5d0b0d'
print(main(379759))   # '0x5cd4f'
print(main(1320643))  # '0x1434db'
print(main(1335658))  # '0x1474ea'
