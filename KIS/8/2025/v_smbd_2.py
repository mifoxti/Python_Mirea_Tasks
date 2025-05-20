def main(bit_fields):
    fields = [int(field, 16) for field in bit_fields]
    Q1 = bin(int(fields[0]))[2:].zfill(4)
    Q2 = bin(int(fields[1]))[2:].zfill(9)
    Q3 = bin(0)[2:].zfill(10)
    Q4 = bin(int(fields[2]))[2:].zfill(6)
    result = str(int(Q4 + Q3 + Q2 + Q1, 2))
    return result


print(main(('0x2', '0x16b', '0x6')))
print(main(('0x3', '0x12b', '0x6')))
