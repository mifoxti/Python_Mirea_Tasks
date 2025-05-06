# from math import ceil
#
#
# def main(N):
#     Phi = {abs(nu) for nu in N if (nu > -83) ^ (nu < -4)}
#     Lambda = {8 * nu + nu ** 2 for nu in N if -56 <= nu < 67}
#     Xi = {7 * phi for phi in Phi if -89 <= phi < 94}
#     union_set = Lambda.union(Xi)
#     union_length = len(union_set)
#     sum_floor_div = sum(ceil(xi / 8) for xi in Xi)
#     theta = union_length + sum_floor_div
#
#     return theta
#
#
# # Test cases
# print(main({67, -29, -25, -86, -18, -67, 29, -75, 59, -3}))  # Expected output: 227
# print(main({-32, 64, 8, 9, 78, -13, -77, 52, -75, 88}))  # Expected output: 275


# def main(zov):
#     putin = {cekc for cekc in zov if -29 < cekc < 50}
#     ylibka = {cekc - cekc % 3 for cekc in zov if cekc <= -11}
#     kiev = putin | ylibka
#     return len(ylibka) + sum(ke for ke in kiev)
#
#
# print(main({-60, -55, 46, -15, 18, -9, 23, -39, -37, -65}))
# print(main({-96, 65, -92, 38, -47, 49, -7, -38, -69, 29}))


# from math import log2
#
#
# def main(y):
#     res = 0
#     n = len(y)
#     for i in range(1, n + 1):
#         res += log2(y[n - i] ** 3 / 85) ** 3
#     return res * 38


def main(x):
    x1_r_r = {1973: 1, 2008: 2}
    x0_u_r = {2015: 3, 1974: 4, 1998: 5}
    x0_b_r = {2015: 7, 1974: 8, 1998: 9}

    x3_m_r = {1990: 0, 2020: x1_r_r[x[1]], 1980: x0_u_r[x[0]]}
    x1_b_m = {1973: x0_b_r[x[0]], 2008: 10}

    x4 = {'TERRA': x3_m_r[x[3]], 'RAGEL': 6, 'LATTE': x1_b_m[x[1]]}
    ini = {2002: x4[x[4]], 1978: 11, 2017: 12}

    return ini[x[2]]
