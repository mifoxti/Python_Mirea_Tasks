from math import ceil


def main(fontan):
    n = {fi for fi in fontan if -57 <= fi <= 50}
    p = {fi ** 3 for fi in fontan if fi < 50}
    k = {5 * pi + pi % 2 for pi in p if (pi < 69 or pi > -51)}

    return len(n | k) + sum([ceil(vi / 8)
                             + ceil(ke / 2)
                             for vi in n for ke in k])


print(main({5, 38, 40, -85, -44, 56, -71, -38, 27, -98})) # = -28718979
print(main({-29, -59, 39, 40, 15, -81, -98, -44, 55, 30}))  # = -24508263
