from math import floor, ceil


def main(omega):
    i = [floor(w / 3) for w in omega if -12 <= w < 43]
    a = [w for w in omega if -94 < w < -7]
    h = {abs(li) + li ** 2 for li in i if -58 <= li < 44}
    k = {9 * ar for ar in a if (ar > 14 or ar < 86)}
    return len(h.union(k)) - sum([ceil(ke / 7) for ke in k])


print(main({58, 10, 75, -18, -41, -11, 23, -38, 60, 31}))
