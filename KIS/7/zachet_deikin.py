def main(x):
    x2_t_r = {2010: 1, 1965: 2}
    x3_m_r = {'PERL6': 3, 'SAS': 4}
    x3_b_r = {'PERL6': 6, 'SAS': 7}

    x1_m_m = {2002: 0, 1974: x2_t_r[x[2]], 1981: x3_m_r[x[3]]}
    x1_b_m = {2002: 5, 1974: x3_b_r[x[3]], 1981: 8}

    x0_l = {2000: x1_m_m[x[1]], 1971: x1_b_m[x[1]]}

    ini = {'CSV': x0_l[x[0]], 'PONY': 9}
    return ini[x[4]]


def main(y):
    n = len(y)
    res = 0
    for i in range(1, n + 1):
        res += (22 * y[n - i] ** 3) ** 5 / 65
    return res * 5
