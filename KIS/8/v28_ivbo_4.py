def main(bit_fields):
    fields = [int(field, 16) for field in bit_fields]
    q1 = bin(0)[2:].zfill(5)
    q2 = bin(int(fields[0]))[2:].zfill(9)
    q3 = bin(int(fields[1]))[2:].zfill(7)
    q4 = bin(int(fields[2]))[2:].zfill(9)
    q5 = bin(int(fields[3]))[2:].zfill(4)
    result = str(hex(int(q5 + q4 + q3 + q2 + q1, 2)))
    return result


main(('0x47', '0x40', '0x26', '0x0'))
main(('0x1c5', '0x74', '0x1a8', '0x6'))
