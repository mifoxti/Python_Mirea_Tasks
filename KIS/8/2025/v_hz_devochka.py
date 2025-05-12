def main(data):
    data = int(data, 16)
    E1 = (data >> 0) & 0b00000000
    E2 = (data >> 8) & 0b1111111
    E3 = (data >> 15) & 0b11
    E4 = (data >> 17) & 0b1111111111
    E5 = (data >> 27) & 0b111111111
    result = ((E5 << 27) | (E2 << 20)
              | (E1 << 12) | (E4 << 2) | E3)
    return str(int(result))


print(main('0x5252f062e'))

print(main('0x7640c86b5'))

print(main('0x5914d9f63'))

print(main('0x325f60881'))
