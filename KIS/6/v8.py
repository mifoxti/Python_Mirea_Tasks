from math import floor


def main(Theta):
    K = {floor(theta / 8) - theta % 2 for theta in Theta if theta < -41 or theta > 65}
    Y = {theta * kappa for theta in Theta for kappa in K if theta > kappa}
    M = {v % 2 + v for v in Y if v <= -52}
    Xi = {abs(kappa) for kappa in K if -59 < kappa <= -9}

    sum_M = sum(floor(mu / 5) for mu in M)
    len_Xi_union_M = len(Xi.union(M))

    epsilon = len_Xi_union_M + sum_M
    return epsilon


print(main({72, 78, -18, 15, -40, 84, 53, 21, 86, -75}))  # должно быть -894
print(main({-92, 13, 14, 47, 49, 84, -42, -8, -71, 88}))  # должно быть -1637
