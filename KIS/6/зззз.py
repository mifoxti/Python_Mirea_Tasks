def main(fontan):
    fu = {2 * v for v in fontan if (v <= 46 ^ v > -51)}
    xi = {abs(v) for v in fontan if v < -66 or v > 23}
    mu = {x for x in xi if x >= 49}
    return len(fu.union(mu)) + sum(mu)


print(main({34, -54, -53, -68, -50, -80, -42, 26, -36, -65}))
print(main({33, 27, -52, -16, 16, -76, 20, 24, -5}))