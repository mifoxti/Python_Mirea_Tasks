from math import ceil


def main(N):
    Phi = {abs(nu) for nu in N if (nu > -83) ^ (nu < -4)}
    Lambda = {8 * nu + nu ** 2 for nu in N if -56 <= nu < 67}
    Xi = {7 * phi for phi in Phi if -89 <= phi < 94}
    union_set = Lambda.union(Xi)
    union_length = len(union_set)
    sum_floor_div = sum(ceil(xi / 8) for xi in Xi)
    theta = union_length + sum_floor_div

    return theta


# Test cases
print(main({67, -29, -25, -86, -18, -67, 29, -75, 59, -3}))  # Expected output: 227
print(main({-32, 64, 8, 9, 78, -13, -77, 52, -75, 88}))  # Expected output: 275
