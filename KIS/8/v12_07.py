def main(data):
    data = int(data)
    i1 = (data >> 0) & 0b1111111
    i2 = (data >> 7) & 0b1111111
    i3 = (data >> 14) & 0b111111
    i4 = (data >> 20) & 0b11111111
    i5 = (data >> 28) & 0b111
    i6 = (data >> 31) & 0b1111111
    result = ((i4 << 29) | (i1 << 22) | (i2 << 15)
              | (i6 << 9) | (i5 << 6) | i3)
    return str(int(result))


print(main(4396612757))
print(main(111551051127))
