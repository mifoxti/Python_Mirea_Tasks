def main(x):
    x3_t_r = {'XML': 0, 'EQ': 1, 'OX': 2}
    x2_tm_r = {1983: 4}

    x2_t_m = {1983: x3_t_r[x[3]]}
    x3_tm_m = {'XML': 3, 'EQ': x2_tm_r[x[2]], 'OX': 5}
    x0_m_m = {2005: 6, 2018: 7}
    x0_b_m = {2005: 9, 2018: 10}

    x1_m_l = {'WISP': x2_t_m[x[2]], 'M': x3_tm_m[x[3]],
              'GDB': x0_m_m[x[0]]}
    x3_b_m = {'XML': 8, 'EQ': x0_b_m[x[0]], 'OX': 11}

    ini = {'ABAP': x1_m_l[x[1]], 'HTTP': x3_b_m[x[3]],
           'XML': 12}
    return ini[x[4]]
