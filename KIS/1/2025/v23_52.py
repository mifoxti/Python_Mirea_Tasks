import math


def main(y):
    numerator = y ** 4 - (y ** 3 - 5) ** 7
    denominator = math.exp(2 * y) + y ** 14
    fraction = numerator / denominator
    first_term = math.sqrt(fraction) if fraction >= 0 else float(
        'nan')
    log_argument = 42 * y ** 3
    if log_argument <= 0:
        return float('nan')
    second_term = (math.log10(log_argument)) ** 5 + 1
    result = first_term - second_term
    return result

print(main(0.58))
print(main(0.18))
print(main(0.88))
print(main(0.33))
print(main(0.6) )