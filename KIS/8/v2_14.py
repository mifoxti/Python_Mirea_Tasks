def main(data):
    data = int(data, 10)

    z1 = (data >> 0) & 0b11

    z2 = (data >> 2) & 0b111111111

    z3 = (data >> 11) & 0b111111111

    z4 = (data >> 20) & 0b11

    z5 = (data >> 22) & 0b1111

    z6 = (data >> 26) & 0b1111

    result = ((z1 << 28) | (z6 << 24) | (z5 << 20) |
              (z2 << 11) | (z3 << 2) | z4)

    return int(result)


# Тестовые примеры
print(main('855386498'))  # 749930007
print(main('196611557'))  # 317443079
print(main('483400688'))  # 121102349
