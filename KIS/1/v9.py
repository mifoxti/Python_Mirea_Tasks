import math


def main(z, x):
    result = (math.log2(x ** 2) + math.log2(z) ** 3 +
              math.sqrt((41 * x) ** 2 - (0.002 + z ** 2 + x ** 3) ** 6))
    return result
