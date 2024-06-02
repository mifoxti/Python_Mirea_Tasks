def main(x):
    x2_t_r = {'GN': 0, 'PAN': 1}
    x2_tm_r = {'GN': 2, 'PAN': 3}
    x2_m_r = {'GN': 4, 'PAN': 5}
    x3_t_l = {1983: x2_t_r[x[2]], 1961: x2_tm_r[x[2]], 1979: x2_m_r[x[2]]}
    x1_m_l = {'LESS': 6, 'KIT': 7}
    x3_d_l = {1983: 8, 1961: 9, 1979: 10}
    ini = {1964: x3_t_l[x[3]], 1965: x1_m_l[x[1]], 2016: x3_d_l[x[3]]}
    return ini[x[0]]
