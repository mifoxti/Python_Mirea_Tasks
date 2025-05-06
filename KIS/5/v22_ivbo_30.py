# from math import log, ceil
#
#
# def main(y, z, x):
#     res = 0
#     n = len(y)
#     for i in range(1, n + 1):
#         res += log(65 * x[i - 1] ** 3 + 62 * z[n - i] ** 2
#                    + 68 * y[ceil(i / 3) - 1]) ** 7
#     res *= 87
#     return res
#
# print(main([0.2, 0.27, 0.46, -0.06],
# [0.33, 0.77, 0.89, -0.78],
# [-0.43, 0.27, -0.54, 0.78]))
# from math import ceil
#
#
# def main(x, y, z):
#     res = 0
#     n = len(y)
#     for i in range(1, n + 1):
#         res += (81 * x[ceil(i / 2) - 1] ** 2
#                 - 90 * z[n - i] ** 3 - y[ceil(i / 3) - 1] / 84)
#     return res * 2
#


def main(x):
    x0_t_r = {1969: 0, 1993: 1, 1968: 2}
    x2_m_r = {'GAMS': 4, 'HACK': 5}
    x3_b_r = {2020: 7, 2016: 8, 1984: 9}

    x3_m_m = {2020: x0_t_r[x[0]], 2016: 3, 1984: x2_m_r[x[2]]}
    x1_b_m = {1975: x3_b_r[x[3]], 1990: 10}

    x1_l = {1975: x3_m_m[x[3]], 1990: 6}
    x0_l = {1969: x1_b_m[x[1]], 1993: 11, 1968: 12}

    ini = {2002: x1_l[x[1]], 1994: x0_l[x[0]], 2006: 13}
    return ini[x[4]]
