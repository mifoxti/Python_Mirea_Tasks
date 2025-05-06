# def main(hex_string):
#     int_value = int(hex_string)
#     x1 = (int_value >> 0) & 0b1111111111
#     x2 = (int_value >> 10) & 0b11
#     x3 = (int_value >> 12) & 0b111
#     x4 = (int_value >> 15) & 0b1111
#     return int(x1), int(x2), int(x3), int(x4)
#
#
# print(main(486161))

# def main(bit_fields):
#     fields = [int(field) for field in bit_fields]
#     q1 = bin(int(fields[0]))[2:].zfill(9)
#     q2 = bin(int(fields[1]))[2:].zfill(6)
#     q3 = bin(int(fields[2]))[2:].zfill(5)
#     q4 = bin(0)[2:].zfill(3)
#     q5 = bin(int(fields[3]))[2:].zfill(10)
#     result = str((int(q5 + q4 + q3 + q2 + q1, 2)))
#     return result
#
#
# print(main((13, 63, 6, 5)))

# def main(data):
#     my_dict = {}
#     for name in data:
#         value = name[1]
#         v = int(value)
#         my_dict[name[0]] = v
#     L1 = bin(int(my_dict['L1']))[2:].zfill(9)
#     L2 = bin(int(my_dict['L1']))[2:].zfill(8)
#     L3 = bin(int(my_dict['L3']))[2:].zfill(8)
#     L4 = bin(int(my_dict['L4']))[2:].zfill(4)
#     L5 = bin(int(my_dict['L5']))[2:].zfill(6)
#     L6 = bin(0)[2:].zfill(5)
#     return str(int(L6 + L5 + L4 + L3 + L2 + L1, 2))
#
#
# print(main([('L1', '99'), ('L2', '247'), ('L3', '80'), ('L4', '9'), ('L5', '46')]))

# from math import sin, ceil
#
#
# def main(y):
#     res = 0
#     n = len(y)
#     for i in range(1, n + 1):
#         res += 46 * sin(y[n - ceil(i / 2)]) ** 3
#     return res


def main(x):
    x0_t_r = {'HY': 0, 'LEAN': 1}
    x0_tm_r = {'HY': 2, 'LEAN': 3}
    x0_mtm_r = {'HY': 4, 'LEAN': 5}
    x1_b_r = {2010: 7, 1960: 8, 1987: 9}

    x3_m_l = {'MESON': x0_t_r[x[0]],
              'LLVM': x0_tm_r[x[0]],
              'ROUGE': x0_mtm_r[x[0]]}

    x0_b_l = {'HY': x1_b_r[x[1]],
              'LEAN': 10}

    ini = {'NU': x3_m_l[x[3]],
           'HLSL': 6,
           'BLADE': x0_b_l[x[0]]}

    return ini[x[2]]
