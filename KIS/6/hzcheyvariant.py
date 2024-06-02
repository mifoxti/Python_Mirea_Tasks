import math
from operator import xor


def main(M):
    Z = {math.floor(mu / 3) - abs(mu) for mu in M if mu < -47}
    T = {mu ** 2 - mu for mu in M if xor(mu < 95, mu >= -7)}
    ohuet = {math.floor(zeta / 5) - abs(zeta)
             for zeta in Z if xor(zeta > -89, zeta < 78)}
    iota = len(T.union(ohuet)) - sum(o ** 3 for o in ohuet)
    return iota


# Примеры результатов вычислений
M1 = {33, -78, -43, 86, -71, 26, -68, -66, -33}
M2 = {89, -62, -56, 78, 16, -78, 25, 23, -71, 30}

print(main(M1))  # Output: 4765678
print(main(M2))  # Output: 3434675
