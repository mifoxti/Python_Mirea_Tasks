def main(x):
    dictx3_up = {1984: 1, 1972: 2}
    dictx1_l_up = {'C': 0, 'GRACE': dictx3_up[x[3]]}

    dictx3_mid = {1984: 3, 1972: 4}
    dictx1_mid = {'C': 5, 'GRACE': 6}

    dictx0_mid_mid = {1961: dictx3_mid[x[3]], 1995: dictx1_mid[x[1]]}

    dictx3_d = {1984: 7, 1972: 8}
    dictx0_d = {1961: 9, 1995: 10}

    dictx1_mid_mid = {'C': dictx3_d[x[3]], 'GRACE': dictx0_d[x[0]]}

    dictx4_mid = {2016: dictx1_l_up[x[1]], 1994: dictx0_mid_mid[x[0]], 2002: dictx1_mid_mid[x[1]]}

    dict_init = {1973: dictx4_mid[x[4]], 1969: 11}

    return dict_init[x[2]]


print(main([1961, 'C', 1969, 1972, 1994]))  # = 11
