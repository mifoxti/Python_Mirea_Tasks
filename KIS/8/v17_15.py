def main(bit_fields):
    fields = [int(field) for field in bit_fields]
    D1 = bin(0)[2:].zfill(0)
    D2 = bin(int(fields[0]))[2:].zfill(4)
    D3 = bin(int(fields[1]))[2:].zfill(8)
    D4 = bin(int(fields[2]))[2:].zfill(2)
    result = str(hex(int(D4 + D3 + D2 + D1, 2)))
    return result


# Test cases
print(main(('5', '118', '1')))

