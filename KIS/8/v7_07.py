def main(data):
    data = int(data, 10)
    N1 = (data >> 0) & 0b00000
    N2 = (data >> 5) & 0b1
    N3 = (data >> 6) & 0b1111
    N4 = (data >> 10) & 0b111
    result = ((N3 << 9) | (N4 << 6) | (N1 << 1) | N2)
    return str(int(result))


print(main('406'))
print(main('7806'))
