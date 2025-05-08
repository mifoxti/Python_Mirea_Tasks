import math


def main(K):
    H = {math.floor(kappa / 3) for kappa in K if kappa < -17}
    Theta = {math.ceil(kappa / 4) for kappa in K if -99 < kappa <= 46}
    Phi = {math.floor(eta / 8) - 4 * eta for eta in H if -67 < eta <= 88}
    Delta = {theta ** 3 for theta in Theta if theta <= 57}
    union_size = len(Delta.union(Phi))
    product = 1
    for phi in Phi:
        product *= (phi % 2)
    omega = union_size + product
    return omega


# Пример 1
print(main({-94, -57, 7, 11, 76, -80, -72, 59}))  # Должно вернуть 10

# Пример 2
print(main({-64, 71, -8, -84, -50, -46, -43, -40, 27, -35}))  # Должно вернуть 15