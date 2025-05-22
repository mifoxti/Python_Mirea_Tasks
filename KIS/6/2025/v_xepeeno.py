import math


def main(M):
    H = {5 * mu - abs(mu) for mu in M if 64 > mu >= -29}
    Phi = {mu % 3 + math.ceil(mu / 2) for mu in M if (mu > 18 or mu < -12)}
    X = {abs(phi) for phi in Phi if -96 <= phi <= 14}
    Omega = {abs(nu) - xe % 3 for nu in H for xe in X if nu < xe}
    nu = len(X) + sum(abs(omega) for omega in Omega)
    return nu


# Примеры вычислений
print(main((33, 2, 42, -49, 15, 49, 83, 25, 27)))  # = 15
print(main((3, -28, -93, 36, 75, 77, -80, -16, 20, -66)))  # = 554
