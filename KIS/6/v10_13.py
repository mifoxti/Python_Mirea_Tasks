def main(M):
    ogo = {abs(u) + abs(u) for u in M if -13 < u < 82}
    p = M | ogo
    omega = ogo | p
    return sum(pi for pi in p) - sum(w % 3 for w in omega)

print(main({-31, -93, 71, -56, -87, -54, -23, 72, 79, -97}))