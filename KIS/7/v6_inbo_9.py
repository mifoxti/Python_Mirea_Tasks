def x1(x, left, mid, right):
    if x[1] == 'HTTP':
        return left
    elif x[1] == 'MIRAH':
        return mid
    elif x[1] == 'ROUGE':
        return right


def x0(x, left, mid, right):
    if x[0] == 1966:
        return left
    elif x[0] == 1992:
        return mid
    elif x[0] == 2015:
        return right


def x3(x, left, mid, right):
    if x[3] == 'ROFF':
        return left
    elif x[3] == 'NINJA':
        return mid
    elif x[3] == 'TCL':
        return right


def x2(x, left, mid, right):
    if x[2] == 1993:
        return left
    elif x[2] == 1987:
        return mid
    elif x[2] == 1960:
        return right


def x4(x, left, mid, right):
    if x[4] == 1994:
        return left
    elif x[4] == 1964:
        return mid
    elif x[4] == 2012:
        return right


def main(x):
    return (x1(x, x0(x, x3(x, 0,
                           x2(x, 1, 2, 3),
                           x2(x, 4, 5, 6)),
                     x4(x, 7,
                        x2(x, 8, 9, 10), 11), 12), 13, 14))
