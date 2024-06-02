def main(x):
    x0_m_r = {2018: 3, 2000: 4}
    x0_m2_r = {2018: 5, 2000: 6}
    x2_m_r = {'KIT': 8, 'FANCY': 9}

    x2_t_r = {'KIT': 0, 'FANCY': 1}
    x2_m_m = {'KIT': x0_m_r[x[0]], 'FANCY': x0_m2_r[x[0]]}

    x1_d_m = {'CMAKE': x2_m_r[x[2]], 'LFE': 10, 'LESS': 11}

    x1_l_m = {'CMAKE': x2_t_r[x[2]], 'LFE': 2, 'LESS': x2_m_m[x[2]]}

    x4_b_l = {'GOSU': x1_d_m[x[1]], 'EBNF': 12}

    init = {1975: x1_l_m[x[1]], 1997: x4_b_l[x[4]], 2015: 7}
    return init[x[3]]


print(main([2018, 'CMAKE', 'KIT', 1975, 'EBNF']))  # = 0
print(main([2018, 'CMAKE', 'FANCY', 1997, 'EBNF']))  # = 12
print(main([2018, 'CMAKE', 'FANCY', 1975, 'GOSU']))  # = 1
print(main([2000, 'LFE', 'KIT', 2015, 'GOSU']))  # = 7
print(main([2000, 'LESS', 'FANCY', 1997, 'GOSU']))  # = 11
