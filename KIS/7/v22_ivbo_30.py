def main(x):
    x1 = {'IDRIS': 0, 'EJS': 1, 'SQLPL': 2}
    x0_m_r = {1961: 3, 2003: 4, 2009: 5}
    x2_b_r = {'PHP': 8, 'MAKO': 9}

    x2_r = {'PHP': x1[x[1]], 'MAKO': x0_m_r[x[0]]}
    x0 = {1961: 6, 2003: 7, 2009: x2_b_r[x[2]]}

    ini = {'EDN': x2_r[x[2]], 'NESC': x0[x[0]]}
    return ini[x[3]]
