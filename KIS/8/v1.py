# def main(data):
#     my_dict = {}
#     for name, value in data:
#         v = int(value, 16)
#         my_dict[name] = v
#     d1 = bin(int(my_dict['O1']))[2:].zfill(8)
#     d2 = bin(int(my_dict['O2']))[2:].zfill(4)
#     d3 = bin(int(my_dict['O3']))[2:].zfill(8)
#     d4 = bin(int(my_dict['O4']))[2:].zfill(6)
#     return str(int(d4 + d3 + d2 + d1, 2))
#
#
# print(type(main([('O1', '0x70'), ('O2', '0x7'), ('O3', '0x12'), ('O4', '0x26')])))  # '39921520'


# print(main([('O1', '0xc'), ('O2', '0xe'), ('O3', '0x79'), ('O4', '0x1f')]))   # '33005068'
# print(main([('O1', '0x2c'), ('O2', '0xb'), ('O3', '0x2a'), ('O4', '0x8')]))    # '8563500'
# print(main([('O1', '0x57'), ('O2', '0x4'), ('O3', '0x17'), ('O4', '0x2')]))     # '2192471'


# def main(hex_str):
#     bin_str = bin(int(hex_str, 16))[2:].zfill(22)
#
#     d4 = bin_str[:6]
#     d3 = bin_str[6:12]
#     d2 = bin_str[12:18]
#     d1 = bin_str[18:22]
#
#     my_dict = [
#         ('I1', hex(int(d1, 2))),
#         ('I2', hex(int(d2, 2))),
#         ('I3', hex(int(d3, 2))),
#         ('I4', hex(int(d4, 2)))
#     ]
#
#     return my_dict
#
#
# # Пример использования
# hex_input = '0x4accb'
# result = main(hex_input)
# print(result)


def main(x):
    x0_t_r = {'SMALI': 0, 'ELM': 1}
    x0_tm_r = {'SMALI': 2, 'ELM': 3}
    x0_m_r = {'SMALI': 4, 'ELM': 5}
    x3_b_r = {2006: 8, 1967: 9}

    x1_l_l = {'FISH': x0_t_r[x[0]], 'APL': x0_tm_r[x[0]],
              'RUST': x0_m_r[x[0]]}

    x0_l = {'SMALI': 7, 'ELM': x3_b_r[x[3]]}

    ini = {1995: x1_l_l[x[x]],
           1985: 6,
           1972: x0_l[x[0]]}

    return ini[x[2]]
