def main(x):
    x3_t_r = {'SASS': 0, 'MUF': 1}
    x1_m_r = {1962: 3, 1994: 4, 1970: 5}

    x0_m_r = {'ABNF': 6, 'FISH': 7, 'PHP': 8}
    x0_d_r = {'ABNF': 9, 'FISH': 10, 'PHP': 11}

    x0_m_t = {'ABNF': x3_t_r[x[3]], 'FISH': 2,
              'PHP': x1_m_r[x[1]]}
    x1_m_d = {1962: x0_m_r[x[0]], 1994: x0_d_r[x[0]],
              1970: 12}

    x2_l = {2014: x0_m_t[x[0]], 1960: x1_m_d[x[1]],
            2015: 13}

    dict_init = {1990: x2_l[x[2]], 1998: 14}

    return dict_init[x[4]]


print(main(['PHP', 1994, 2014, 'SASS', 1998]))  # = 14