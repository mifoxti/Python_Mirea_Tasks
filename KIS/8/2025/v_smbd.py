def main(data):
    data = int(data)
    Z1 = (data >> 0) & 0b11111
    Z2 = (data >> 5) & 0b111111
    Z3 = (data >> 11) & 0b0000000
    Z4 = (data >> 18) & 0b111
    Z5 = (data >> 21) & 0b11111
    Z6 = (data >> 26) & 0b1111
    result = ((Z3 << 23) | (Z2 << 17)
              | (Z5 << 12) | (Z1 << 7) | (Z4 << 4) | Z6)
    return str(hex(int(result)))


print(main('312060649'))

print(main('535718501'))

print(main('758919944'))

print(main('405602084'))
