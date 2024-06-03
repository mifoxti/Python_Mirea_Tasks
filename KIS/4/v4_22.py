def main(n):
    if n == 0:
        return -0.16
    elif n == 1:
        return 0.44
    elif n >= 2:
        return main(n - 1) ** 2 - 1 - main(n - 2) / 66
