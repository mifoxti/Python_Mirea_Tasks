from math import ceil


def main(T):
    Lambda = {7 * tau for tau in T if -25 <= tau <= 70}
    H = {5 * lam for lam in Lambda if (lam >= 38 or lam <= -77)}
    B = {abs(tau) + tau ** 2 for tau in T if tau > 8}
    N = B | H
    sum1 = sum(ceil(eta / 6) for eta in H)
    sum2 = sum(eta * nu for eta in H for nu in N)

    return sum1 - sum2


print(main([-96, -60, -27, 39, 42, -52, -73, -38, 59, -66]))  # -57848582
print(main([36, -23, -54, 44, -15, 29, 53, -3, -2]))          # -49405834
