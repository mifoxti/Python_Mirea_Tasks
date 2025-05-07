from math import ceil


def main(x, y, z):
    n = len(z)
    sum = 0
    for i in range(1, n + 1):
        sum += (y[n - i] ** 2 + 27 * z[n - ceil(i / 2)]
                + 8 * x[n - ceil(i / 2)] ** 3) ** 5
    return sum


print(f'= {main([0.71, -0.89],
                [-0.61, -0.84],
                [-0.58, -0.5]):.2e}')
