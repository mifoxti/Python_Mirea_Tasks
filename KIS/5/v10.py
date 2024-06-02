from math import ceil


def main(y, x):
    n = len(x)
    sum_value = 0
    for i in range(1, n + 1):
        term1 = 16 * x[n - i]
        term2 = (x[n - i] ** 2) / 35
        term3 = 93 * (y[ceil(i / 4 - 1)] ** 3)
        sum_value += 67 * (term1 - term2 - term3) ** 7
    result = 63 * sum_value
    return result


# Test examples
examples = [
    ([0.84, -0.39, -0.1, 0.83, 0.29, 0.42, -0.15],
     [0.91, -0.37, -0.65, 0.44, -0.56, -0.35, -0.17]),
    ([-0.36, 0.51, 0.89, 0.32, 0.42, -0.07, -0.28],
     [-0.34, 0.86, 0.35, 0.25, 0.41, -0.74, -0.68]),
    ([-0.62, 0.48, 0.84, 0.78, -0.93, 0.71, 0.58],
     [0.32, -0.11, 0.71, 0.38, 0.78, 0.92, 1.0]),
    ([-0.13, 0.43, 0.65, -0.54, -0.0, 0.68, -0.47],
     [-0.76, -0.29, 0.33, 0.37, 0.11, -0.3, 0.27])
]

for example in examples:
    y, x = example
    print(f"f({y}, {x}) = {main(y, x)}")
