def main(data):
    data = int(data, 10)
    z1 = (data >> 0) & 0b111
    z2 = (data >> 3) & 0b11111
    z3 = (data >> 8) & 0b111
    z4 = (data >> 11) & 0b11111111

    result = ((z2 << 14) | (z1 << 11) | (z4 << 3) | z3)

    return int(result)

print(main('423111'))
print(main('405342'))
