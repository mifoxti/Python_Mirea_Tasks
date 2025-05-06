# def main(hex_string):
#     int_value = int(hex_string, 16)
#     v1 = (int_value >> 0) & 0b1
#     v2 = (int_value >> 1) & 0b11111111
#     v3 = (int_value >> 9) & 0b1111111
#     v4 = (int_value >> 16) & 0b111111111
#     v5 = (int_value >> 25) & 0b1111111
#     return {'V1': str(hex(v1)), 'V3': str(hex(v3)),
#             'V4': str(hex(v4)), 'V5': str(hex(v5))}
#
#
# print(main('0x6797ca22'))
#

# def main(hex_string):
#     int_value = int(hex_string)
#     Y1 = (int_value >> 0) & 0b1
#     Y2 = (int_value >> 1) & 0b1
#     Y3 = (int_value >> 2) & 0b11111111
#     Y4 = (int_value >> 10) & 0b0000000000
#     return {'Y1': str(int(Y1)), 'Y2': str(int(Y2)),
#             'Y3': str(int(Y3))}
#
#
# print(main('691'))


def main(bit_fields):
    fields = [int(field) for field in bit_fields]
    M1 = bin(int(fields[0]))[2:].zfill(2)
    M2 = bin(int(fields[1]))[2:].zfill(8)
    M3 = bin(int(fields[2]))[2:].zfill(7)
    M4 = bin(0)[2:].zfill(8)
    M5 = bin(int(fields[3]))[2:].zfill(7)
    result = str(int(M5 + M4 + M3 + M2 + M1, 2))
    return result


main(('1', '47', '59', '83'))
main(('3', '86', '49', '5'))
