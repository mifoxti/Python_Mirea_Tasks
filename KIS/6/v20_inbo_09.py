def main(K):
    A = {7 * k for k in K if k <= -72 or k >= 2}
    Delta = {7 * k for k in K if -62 < k < 54}
    B = {delta % 2 + 8 * alpha for delta in Delta
         for alpha in A if delta >= alpha}
    sum_alpha_mod_2 = sum(alpha % 2 for alpha in A)
    sum_abs_beta = sum(abs(beta) for beta in B)
    zeta = sum_alpha_mod_2 + sum_abs_beta
    return zeta


# Example usage:
print(main([-64, 1, 9, 81, -45, -75, -10, -38]))  # Should return 8907
print(main([-84, -20, -50, -81, 47, 50, 20, 84, 27, 30]))  # Should return 35173
