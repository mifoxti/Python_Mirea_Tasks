def main(x):
    x0_u_r = {1981: 0, 2003: 1}
    x0_m_r = {1981: 2, 2003: 3}
    x3_d_r = {'NINJA': 5, 'PERL': 6, 'JSX': 7}

    x3_m_m = {'NINJA': x0_u_r[x[0]], 'PERL': x0_m_r[x[0]], 'JSX': 4}

    x1_d_m = {1997: x3_d_r[x[3]], 1985: 8, 1964: 9}

    x2 = {'TXL': x3_m_m[x[3]], 'COQ': x1_d_m[x[1]]}
    return x2[x[2]]

print(main([1981, 1997, 'TXL', 'JSX']))