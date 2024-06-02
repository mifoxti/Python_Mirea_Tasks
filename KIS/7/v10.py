def main(x):
    x1_t_r = {2002: 1, 2017: 2}
    x1_mt_r = {2002: 4, 2017: 5}
    x1_m_r = {2002: 6, 2017: 7}

    x2_b_r = {'BLADE': 8, 'VALA': 9, 'GN': 10}

    x4_t_m = {'MIRAH': 0, 'RUBY': x1_t_r[x[1]]}
    x4_m = {'MIRAH': x1_mt_r[x[1]], 'RUBY': x1_m_r[x[1]]}
    x4_b = {'MIRAH': x2_b_r[x[2]], 'RUBY': 11}

    x2_m_l = {'BLADE': x4_t_m[x[4]], 'VALA': 3, 'GN': x4_m[x[4]]}
    x3_b_l = {'LSL': x4_b[x[4]], 'D': 12}

    ini = {'OCAML': x2_m_l[x[2]], 'GLSL': x3_b_l[x[3]], 'BRO': 13}
    return ini[x[0]]
