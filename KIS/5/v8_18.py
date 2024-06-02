def main(y, z, x):
    res = 0
    n = len(y)
    for i in range(1, n + 1):
        res += (x[n - i] ** 2 - z[i - 1] ** 3 - 44 * y[n - i]) ** 6
    return res * 69
