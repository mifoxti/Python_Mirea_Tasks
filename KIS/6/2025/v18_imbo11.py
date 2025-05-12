from math import floor


def main(psi_set):
    omega = {floor(c / 9) + c for c in psi_set if (c < -8) ^ (c > -52)}
    T = {psi for psi in psi_set if psi < 37 or psi >= 55}
    H = T.union(omega)
    M = {7 * w for w in omega if -15 <= w <= 78}
    epsilon = len(H) * len(M) - sum(mu % 2 for mu in M)
    return epsilon


print(main({64, -38, 72, 73, 12, 80, -75, 90, -1, -97}))  # → 52
print(main({4, 39, 72, 71, 8, 44, 15, -9, -40, -71}))  # → 83
