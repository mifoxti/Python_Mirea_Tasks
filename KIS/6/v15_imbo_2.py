from operator import xor


def main(heta):
    oka = {6 * n for n in heta if n > -82 or n <= 38}
    xeta = {n ** 2 for n in heta if xor(n >= -87, n < 23)}
    eta = oka.union(xeta)
    return (len(xeta)
            - sum([abs(xi) - 9 * ee for xi in xeta for ee in eta]))


print(main({-29, 68, 37, 38, 70, -54, -53, 45, -18, -2}))
print(main({-96, -88, -83, -78, 83, -77, -34, 62, -3, -1}))