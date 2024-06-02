def main(x):
    x3_t_r = {'TCL': 1}
    x2_tm_r = {'HCL': 2, 'CUDA': 3}
    x3_m_r = {'TCL': 5}
    x3_mb_r = {'TCL': 7}
    x3_b_r = {'TCL': 8}

    x1_t_m = {2017: 0, 1964: x3_t_r[x[3]]}
    x3_mt_m = {'TCL': x2_tm_r[x[2]]}
    x1_m_m = {2017: 4, 1964: x3_m_r[x[3]]}
    x1_b_m = {2017: x3_mb_r[x[3]], 1964: x3_b_r[x[3]]}

    x0_m_l = {'RAML': x1_t_m[x[1]], 'M': x3_mt_m[x[3]],
              'HTML': x1_m_m[x[1]]}
    x0_b_l = {'RAML': 6, 'M': x1_b_m[x[1]], 'HTML': 9}

    ini = {1976: x0_m_l[x[0]], 1986: x0_b_l[x[0]]}
    return ini[x[4]]


print(main(['HTML', 1964, 'CUDA', 'TCL', 1986]))