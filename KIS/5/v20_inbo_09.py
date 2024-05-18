from math import floor


def main(y, z, x):
    n = len(y)
    res = 0
    for i in range(1, n+1):
        res += floor(y[n - i] ** 3 - 5 * z[n-i] ** 2 - x[i-1]) ** 2
    res *= 41
    return res

data = [[0.3, 0.88, 0.27, -0.2],
[0.67, 0.12, -0.22, -0.69],
[0.16, 0.93, 0.26, 0.88]]
print(f'= {main(data[0], data[1], data[2]):.2e}')