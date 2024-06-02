def main(n):
    if n == 0:
        return -0.36
    elif n >= 1:
        return 1 - main(n - 1) ** 3 - main(n - 1) ** 2
