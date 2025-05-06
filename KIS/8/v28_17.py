def main(bit_fields):
    fields = [int(field) for field in bit_fields]
    R1 = bin(int(fields[0]))[2:].zfill(10)
    R2 = bin(0)[2:].zfill(7)
    R3 = bin(int(fields[1]))[2:].zfill(7)
    R4 = bin(int(fields[2]))[2:].zfill(1)
    R5 = bin(int(fields[3]))[2:].zfill(4)
    R6 = bin(int(fields[4]))[2:].zfill(5)
    result = str(hex(int(R6 + R5 + R4 + R3 + R2 + R1, 2)))
    return result


print(main(('361', '67', '1', '6', '30')))
print(main(('434', '33', '1', '13', '21')))