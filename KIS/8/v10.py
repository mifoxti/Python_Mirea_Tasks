def main(data):
    data = int(data)
    Z1 = (data >> 0) & 0b11
    Z2 = (data >> 2) & 0b11
    Z3 = (data >> 4) & 0b0
    Z4 = (data >> 5) & 0b111111
    result = ((Z2 << 9) | (Z4 << 3) | (Z1 << 1) | Z3)
    return str(int(result))


print(main('1416'))
print(main('258'))
