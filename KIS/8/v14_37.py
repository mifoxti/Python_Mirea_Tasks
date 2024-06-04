def main(bit_fields):
    fields = [int(field) for field in bit_fields]
    J1 = bin(0)[2:].zfill(3)
    J2 = bin(int(fields[0]))[2:].zfill(6)
    J3 = bin(int(fields[1]))[2:].zfill(4)
    J4 = bin(int(fields[2]))[2:].zfill(6)
    J5 = bin(int(fields[3]))[2:].zfill(2)
    J6 = bin(int(fields[4]))[2:].zfill(7)
    result = str(hex(int(J6 + J5 + J4 + J3 + J2 + J1, 2)))
    return result


main(('36', '11', '12', '1', '126'))
main(('14', '1', '34', '2', '75'))
main(('14', '8', '25', '1', '114'))
main(('4', '14', '53', '3', '60'))
