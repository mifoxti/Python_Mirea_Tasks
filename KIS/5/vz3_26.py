from math import ceil


def main(x, y):
    n = len(y)
    res = 0
    for i in range(1, n + 1):
        res += 69 * (0.03 + 17 * x[n - ceil(i / 2)] ** 2
                     + y[i - 1]) ** 3
    return res * 80


print(main([0.16, 0.08, -0.78],
           [-0.71, -0.63, 0.77]))
print(main([0.07, 0.42, 0.93],
           [0.29, -0.57, -0.77]))
print(main([-0.06, -0.58, 0.53],
           [0.34, -0.33, 0.38]))
print(main([0.39, -0.83, -0.78],
           [-0.35, 0.23, 0.41]))
print(main([-0.09, -0.6, 0.12],
           [0.15, 0.66, -0.89]))
