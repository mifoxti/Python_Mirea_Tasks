def main(n):
    if n == 0:
        return -0.06
    elif n == 1:
        return 0.13
    elif n >= 2:
        return 1 - main(n - 1) - main(n - 2) ** 2


print(main(5))
print(main(6))
print(main(9))
print(main(2))
print(main(7))