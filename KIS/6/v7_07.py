def main(N):
    Lambda = {abs(nu) - nu ** 2 for nu in N if nu <= 20 or nu >= -88}
    T = {6 * nu + abs(nu) for nu in N if nu < 48 and nu >= -33}
    E = {tau // 5 for tau in T if tau > -40 or tau <= -8}
    Z = Lambda.union(T)
    chi = len(Z) - sum(epsilon ** 3 for epsilon in E)
    return chi


# Примеры использования функции
print(main({-95, 44, -48, 80, -75, 86, -43, -39, 92, 63}))  # = -226970
print(main({2, -29, 10, -54, 45, -78, -13, 82, 91, -3}))  # = -226170
