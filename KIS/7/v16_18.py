def main(x):
    x1_t_r = {1969: 0, 1985: 1}
    x1_mt_r = {1969: 2, 1985: 3}
    x0_m_r = {1999: 4, 2002: 5, 1957: 6}

    x0_b_r = {1999: 9, 2002: 10, 1957: 11}

    x3_mt_m = {'IDL': x1_t_r[x[1]], 'COQ': x1_mt_r[x[1]],
               'GN': x0_m_r[x[0]]}

    x3_mb_m = {'IDL': 7, 'COQ': 8, 'GN': x0_b_r[x[0]]}

    x4_l = {'WISP': x3_mt_m[x[3]], 'RAGEL': x3_mb_m[x[3]],
            'MUF': 12}

    ini = {'GAMS': x4_l[x[4]], 'ELM': 13}

    return ini[x[2]]
