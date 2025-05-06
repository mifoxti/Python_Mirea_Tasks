# def main(value):
#     int_value = int(value)
#     R1 = (int_value >> 0) & 0b000000
#     R2 = (int_value >> 6) & 0b1111111111
#     R3 = (int_value >> 16) & 0b1
#     R4 = (int_value >> 17) & 0b111
#     R5 = (int_value >> 20) & 0b11
#     R6 = (int_value >> 22) & 0b111
#     return R2, R3, R4, R5, R6
#
#
# print(main(4806224))
#
# print(main(9278646))
#
# print(main(10893862))
#
# print(main(9654455))


def main(value):
    int_value = int(value)
    E1 = (int_value >> 0) & 0b1111111111
    E2 = (int_value >> 10) & 0b1111111111
    E3 = (int_value >> 20) & 0b1111
    E4 = (int_value >> 24) & 0b000000000
    E5 = (int_value >> 33) & 0b11111
    return str(hex(E1)), str(hex(E2)), str(hex(E3)), str(hex(E5))


print(main('106522792656'))

print(main('169609358589'))

print(main('262665956324'))

print(main(9654455))
