def main(x, y, z):
    n = len(x)
    result = 0
    for i in range(1, n + 1):
        inner_sum = (94 * (x[i - 1] ** 2 + z[n - i] ** 3 + 80 * y[i - 1]))
        result += inner_sum
    result *= 6
    return result


data = ([-0.28, -0.58, -0.62, 0.38, 0.22],
[-0.99, -0.06, 0.25, 0.43, 0.94],
[0.32, 0.6, -0.95, -0.56, 0.77])

print(f'= {main(data[0], data[1], data[2]):.2e}')
