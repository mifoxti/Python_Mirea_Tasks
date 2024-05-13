def main(x):
    dict_x3_u_r = {'FREGE': 1, 'KRL': 2}
    dict_x2_u_r = {1988: 4, 1983: 5}
    dict_x2_m_r = {1988: 6, 1983: 7}

    dict_x2_u_m = {1988: 0, 1983: dict_x3_u_r[x[3]]}
    dict_x1_m_m = {1973: dict_x2_u_r[x[2]],
                   2015: dict_x2_m_r[x[2]], 1998: 8}

    dict_x4_m_d = {'TEA': 9, 'CIRRU': 10, 'FORTH': 11}

    dict_x4_u_l = {'TEA': dict_x2_u_m[x[2]], 'CIRRU': 3,
                   'FORTH': dict_x1_m_m[x[1]]}

    dict_x3_d_m = {'FREGE': dict_x4_m_d[x[4]], 'KRL': 12}

    dict_init = {2002: dict_x4_u_l[x[4]],
                 1970: dict_x3_d_m[x[3]], 1964: 13}

    return dict_init[x[0]]

print(main([1964, 1973, 1983, 'FREGE', 'CIRRU']))
print(main([1970, 1973, 1988, 'KRL', 'FORTH']))
