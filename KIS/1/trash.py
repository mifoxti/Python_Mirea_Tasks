# from math import ceil, atan
#
#
# def main(x, y, z):
#     a = z ** 2 / 32 + 4 * (ceil(0.01 - x ** 2 - y ** 3 / 31)) ** 3
#     b = (atan(68 * y + 85 + x ** 2)) ** 4 - 19 * (70 * z ** 3) ** 7
#     c = a + b
#     return c


# from math import sin
#
#
# def main(x):
#     if x < -33:
#         return 93 * x ** 2 - 30 * sin(x) - 72
#     elif -33 <= x < 59:
#         return 64 * x ** 3 - 0.12 - (x ** 2 + x ** 3 + x) ** 6
#     elif x >= 59:
#         return x


# def main(n):
#     if n == 0:
#         return -0.23
#     elif n >= 1:
#         return (main(n - 1)) ** 3 + (main(n - 1)) ** 2 / 87 + main(n - 1)

# def main(n):
#     if n == 0:
#         return -0.23
#     elif n >= 1:
#         return (main(n - 1)) ** 3 + (main(n - 1)) ** 2 / 87 + main(n - 1)


# import math
#
#
# def main(y):
#     res = 0
#     n = len(y)
#     for i in range(1, n + 1):
#         res += (math.sqrt(y[n - math.ceil(i / 4)] ** 3 / 77)) ** 4
#     return 66 * res

#
# import operator
#
#
# def main(z):
#     a = {2 * c - 6 * c for c in z if -11 < c <= 34}
#     f = {2 * c + 5 * c for c in z if c < 39}
#     t = {abs(fm) + abs(fm) for fm in f if (operator.xor((fm < 12), fm > -98))}
#     v = len(a | t) - sum(abs(am) + 7 * tm for am in a for tm in t)
#     return v


# def x0(x, right, mid, left):
#     if x[0] == 1971:
#         return right
#     elif x[0] == 1983:
#         return mid
#     elif x[0] == 2000:
#         return left
#
#
# def x1(x, right, mid, left):
#     if x[1] == 2016:
#         return right
#     elif x[1] == 1993:
#         return mid
#     elif x[1] == 1968:
#         return left
#
#
# def x2(x, right, left):
#     if x[2] == 2017:
#         return right
#     elif x[2] == 2002:
#         return left
#
#
# def x4(x, right, left):
#     if x[4] == 1964:
#         return right
#     elif x[4] == 1965:
#         return left
#
#
# def x3(x, right, left):
#     if x[3] == "TCL":
#         return right
#     elif x[3] == "OPAL":
#         return left
#
#
# def main(x):
#     return (x0(x, x1(x, x2(x, x4(x, 0, 1),
#                            x4(x, 2, 3)),
#                      x3(x, 4, 5), x2(x, 6,
#                                      x4(x, 7, 8))), 9, 10))


# from math import ceil
#
#
# def main(z, y):
#     n = len(y)
#     res = 0
#     for i in range(1, n + 1):
#         res += 87 * (7 * z[n - ceil(i / 4)] - 1 - y[ceil(i / 4) - 1] ** 3) ** 5
#     return 62 * res
