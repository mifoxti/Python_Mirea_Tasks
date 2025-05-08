import math


def main(n):
    if n == 0:
        return 0.94
    else:
        f_prev = main(n - 1)
        term = 0.01 + 83 * f_prev + 72 * f_prev ** 2
        log_term = (math.log2(term)) ** 3 if term > 0 else float('nan')
        result = log_term + 8 + math.cos(f_prev)
        return result
