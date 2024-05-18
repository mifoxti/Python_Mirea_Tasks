def main(data):
    data = int(data)
    d1 = (data >> 0) & 0b1111
    d2 = (data >> 4) & 0b00
    d3 = (data >> 6) & 0b1111111
    d4 = (data >> 13) & 0b11111

    result = ((d2 << 16) | (d1 << 12) | (d3 << 5) | d4)
    return str(int(result))


print(main(112491))