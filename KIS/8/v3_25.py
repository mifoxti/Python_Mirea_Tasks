def main(data):
    R1 = (data >> 0) & 0b111111111
    R2 = (data >> 9) & 0b11
    R3 = (data >> 11) & 0b11111111
    R4 = (data >> 19) & 0b111111111
    R5 = (data >> 28) & 0b111111
    R6 = (data >> 34) & 0b111111
    result = ((R3 << 31) | (R2 << 29)
              | (R6 << 24) | (R5 << 18)
              | (R4 << 9) | R1)
    return str(int(result))


print(main(446139017796))
print(main(174709002121))