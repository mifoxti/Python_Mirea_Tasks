def main(x):
    if x == 0:
        return -0.04
    elif x >= 1:
        return main(x - 1) - 21 * main(x - 1) ** 3
