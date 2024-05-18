def main(data):
    data = int(data)
    m1 = (data >> 0) & 0b1111
    m2 = (data >> 4) & 0b111111
    m3 = (data >> 10) & 0b11111111
    m4 = (data >> 18) & 0b000000000

    result = ((m1 << 23) | (m3 << 15) | (m4 << 6) | m2)
    return int(result)


print(main('148539'))