def main(data):
    data = int(data, 10)
    z1 = (data >> 0) & 0b1111111111
    z2 = (data >> 10) & 0b1111111111
    z3 = (data >> 20) & 0b11
    z4 = (data >> 22) & 0b11111111
    z5 = (data >> 30) & 0b1111111111
    z6 = (data >> 40) & 0b1111111111

    result = ((z5 << 39) | (z2 << 29) | (z1 << 19)
              | (z4 << 11) | (z6 << 2) | z3)

    return int(result)


print(main('532216460737337'))
print(main('355657917685958'))
