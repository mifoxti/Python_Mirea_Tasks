from math import floor


def main(fontan):
    P = [v ** 2 for v in fontan if v < -26]
    OGO = [floor(p / 7) for p in P if (p >= -99 or p <= 44)]
    H = [v ** 3 for v in fontan if (v <= 65 or v >= -59)]
    K = [n for n in H if n not in range(-54, 82)]

    SigmaO = sum([3 * o for o in OGO])
    Sigma = sum([6 * o - floor(k / 8) for o in OGO for k in K])
    return SigmaO + Sigma


print(main({-94, 3, 6, 41, 45, 46, 17, -41, 91, 63}))
print(main({32, -63, 68, 74, -86, -15, 82, -71, -99, -66}))
