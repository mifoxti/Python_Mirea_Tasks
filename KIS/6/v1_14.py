def main(E):
    B = {3 * e - abs(e) for e in E if e > -76}
    Y = {abs(e) for e in E if e > -91 or e <= 22}
    Ogo = {u * v for u in Y for v in B if u > v}
    kappa = len(B) * len(Ogo) + sum(7 * theta for theta in Ogo)
    return kappa


# Примеры использования функции
print(main({-29, 36, 9, 12, -19, -20, -46, 58, -66, -33}))  # = -1311430
print(main({65, -63, 74, 13, 47, -78, 84, -12, 26, 63}))  # = -741482
