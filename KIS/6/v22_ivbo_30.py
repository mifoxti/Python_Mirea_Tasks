


# def main(kiev):
#     nash_slon = {ke % 2 - ke for ke in kiev if (ke >= -69 or ke < -7)}
#     zov = {ke * v for ke in kiev for v in nash_slon if ke < v}
#     bet = nash_slon.union(zov)
#
#     zub = len(zov.union(bet))
#     res = sum([floor(b / 5) for b in bet])
#     return res + zub
#
# print(main({96, 65, -93, -56, -88, -16, 81, 93, 30, 95}))
# print(main({-95, 98, 68, -55, 75, 12, -83, 24, 91}))
#

from math import ceil, floor
from operator import xor


def main(A):
    igi = {5 * ar + ceil(ar / 5) for ar in A if xor(ar > -56, ar <= 5)}
    fi = {ar * i for ar in A for i in igi if ar <= i}
    font = {i ** 3 for i in igi if i <= 32}
    return sum([o % 3 for o in fi]) - sum(floor(vi / 7) for vi in font)


print(main({-29, 35, 39, -55, 41, 43, 14, -82, 83, 60}))
print(main({-94, 3, 90, 11, 86, -41, 58, -69, -4, -99}))