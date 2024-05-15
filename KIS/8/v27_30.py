def main(data):
    data = int(data)
    z1 = (data >> 0) & 0b1111
    z2 = (data >> 4) & 0b1111
    z3 = (data >> 8) & 0b11111111
    z4 = (data >> 16) & 0b111111111
    result = ((z4 << 16) | (z2 << 12) | (z3 << 4) | z1)
    return str(int(result))

print(main(4894072))
print(main(17834932))
