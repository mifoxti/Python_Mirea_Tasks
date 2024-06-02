def main(Phi):
    N = {abs(phi) for phi in Phi if -84 < phi < 44}
    P = {14 * nu for nu in N if -7 <= nu < 35}
    X = {phi ** 3 + 3 * nu for phi in Phi for nu in N if phi <= nu}
    ibatmoihuy = {abs(chi) + rho ** 2 for chi in X for rho in P if chi >= rho}
    kappa = len(P.union(ibatmoihuy)) - sum(lublu % 2 for lublu in ibatmoihuy)
    return kappa


# Примеры результатов вычислений
Phi1 = {65, 33, 4, 68, 75, 81, 22, 56, 57, -99}
Phi2 = {72, 43, 80, 49, 17, 56, -71, -37}

print(main(Phi1))  # Output: 11
print(main(Phi2))  # Output: 8
