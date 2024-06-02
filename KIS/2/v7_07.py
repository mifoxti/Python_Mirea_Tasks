def main(x):
    if x < 105:
        return 8 - x / 50 - 78 * x ** x - 19
    elif 105 <= x < 153:
        return ((x ** 2 / 92 + 47 + 89 * x) ** 7
                - (27 * x ** 2 - x) ** 6 - (x / 79) ** 5)
    elif 153 <= x < 169:
        return x ** 12 + x
    elif 169 <= x < 211:
        return x ** 6
    elif x >= 211:
        return 85 * x ** 3
