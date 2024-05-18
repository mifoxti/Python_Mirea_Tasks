from math import acos


def main(y, z, x):
    un_1 = (51 * (16 - x ** 3 - 76 * y) ** 4
            - 39 * (51 + 22 * z + 7 * y ** 3) ** 3) / (
                66 * (71 * x ** 2 - 28 * z) ** 7 + 24 * y)

    un_2 = 45 * acos((y ** 2 / 27) + z + 66 * x ** 3) ** 5
    return un_1 + un_2


print(main(-0.96, 0.54, -0.16))
print(main(0.03, -0.95, -0.05))
print(main(0.07, 0.24, 0.14))
print(main(0.94, -0.28, -0.2))
