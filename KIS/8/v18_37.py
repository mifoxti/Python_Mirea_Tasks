def main(data):
    X1 = (data >> 0) & 0b11111
    X2 = (data >> 5) & 0b111
    X3 = (data >> 8) & 0b1111111
    X4 = (data >> 15) & 0b1
    X5 = (data >> 16) & 0b11111
    result = ((X4 << 20) | (X5 << 15) | (X1 << 10) | (X2 << 7) | X3)
    return str(int(result))


print(main(1591003))
print(main(1830654))
