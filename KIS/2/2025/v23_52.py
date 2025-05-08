from math import ceil


def main(Y):
    H = {abs(v) for v in Y if 26 > v > -19}
    Psi = {eta - ceil(eta / 6) for eta in H if eta > -73}
    X = {4 * v + v ** 2 for v in Y if v < 64 and v >= -11}
    Z = X.union(H)
    cross_product_size = len(Z) * len(Psi)
    sum_psi = sum(7 * psi for psi in Psi)
    phi = cross_product_size + sum_psi
    return phi


print(main({96, -28, 36, 6, -60, 73, 10, -73, -36, -67}))
print(main({-96, 3, -57, 73, -87, -21, -79, 21, -8, 91}))
