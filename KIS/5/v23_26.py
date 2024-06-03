from math import atan, ceil


def main(y):
    n = len(y)
    sum1 = 0
    for i in range(1, n + 1):
        sum1 += atan(y[n - i] ** 2 + y[n - ceil(i / 2)]) ** 4 / 67
    return sum1


print(main([0.79, -0.77]))
print(main([0.6, -0.54]))
print(main([0.79, 0.62]))
print(main([0.0, 0.81]))
print(main([-0.15, 0.87]))