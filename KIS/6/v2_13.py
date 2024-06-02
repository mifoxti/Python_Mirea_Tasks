from math import floor


def main(A):
    Delta = {floor(alpha // 9) - 8 * alpha for alpha in A
             if alpha <= 40 or alpha >= -73}
    Psi = A.union(Delta)
    Phi = {abs(delta) + delta ** 2 for delta in Delta
           if delta < -76}
    Ypsilon = {psi for psi in Psi if -70 < psi < 48}
    Phi_cross_Ypsilon = {(phi, ypsilon) for phi in Phi
                         for ypsilon in Ypsilon}
    theta = len(Phi_cross_Ypsilon) + sum(phi * ypsilon
                                         for phi, ypsilon
                                         in Phi_cross_Ypsilon)
    return theta


# Примеры вычислений
print(main({-90, -49, -46, 18, 20, 53, -13, -72, -70, 92}))  # Ожидаемый результат: -52444680
print(main({7, 72, 40, -82, 80, 51, -44, 56, -67, 30}))  # Ожидаемый результат: -111459924
