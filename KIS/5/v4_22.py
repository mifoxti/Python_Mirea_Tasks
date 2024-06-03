from math import floor


def main(treugolnik):
    pizda = {be for be in treugolnik if be >= 39}
    titki = {5 * p for p in pizda if -83 < p <= 77}
    xui = {floor(be / 2) + be % 3 for be in treugolnik if -81 <= be <= 42}
    figura = {7 * x for x in xui if -64 <= x < 37}

    return len([a * b for a in figura for b in titki]) - sum(titki)
