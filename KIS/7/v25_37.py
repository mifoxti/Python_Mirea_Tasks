def main(x):
    dictx4_up = {2000: 0, 1982: 1}
    dictx3_m_up = {1969: 2, 1964: 3, 1958: 4}

    dictx1_mid = {'SMALI': dictx4_up[x[4]],
                  'VUE': dictx3_m_up[x[3]], 'MAX': 5}

    dictx2_mid_l = {1962: dictx1_mid[x[1]], 2005: 6}

    dictx4_mid_l_d = {2000: 7, 1982: 8}

    dict_init = {1985: dictx2_mid_l[x[2]],
                 2003: dictx4_mid_l_d[x[4]], 1963: 9}

    return dict_init[x[0]]


print(main([2003, 'SMALI', 1962, 1964, 2000]))  # = 7
