from math import floor, ceil


def main(fi):
    ni = {o % 2 - o for o in fi if -75 < o < 59}
    li = {f * v for f in fi for v in ni if f < v}
    xi = {floor(alpha / 8) for alpha in li if (alpha > -39 or alpha <= 25)}
    ii = ni.union(li)

    return len([ig for ig in ii]) + sum([ceil(x / 3) for x in xi])


print(main({37, -91, 75, -52, -51, -45, -76, -74, -38, 59}))
print(main({33, -25, 40, 73, 47, 53, -73, 56, -38, 30}))
