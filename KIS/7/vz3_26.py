def main(x):
    x1_t_r = {'P4': 0, 'PIKE': 1}
    x0_tm_r = {'DM': 2, 'E': 3}
    x2_bm_r = {'STATA': 5, 'ATS': 6,
               'TERRA': 7}
    x1_b_r = {'P4': 8, 'PIKE': 9}

    x2_m_l = {'STATA': x1_t_r[x[1]], 'ATS': x0_tm_r[x[0]],
              'TERRA': 4}
    x0_m_l = {'DM': x2_bm_r[x[2]],
              'E': x1_b_r[x[1]]}

    ini = {'ROUGE': x2_m_l[x[2]],
           'DART': x0_m_l[x[0]],
           'SMALI': 10}
    return ini[x[3]]


print(main(['E', 'PIKE', 'ATS', 'DART']))
print(main(['E', 'P4', 'ATS', 'DART']))
print(main(['DM', 'PIKE', 'TERRA', 'DART']))
print(main(['DM', 'P4', 'TERRA', 'ROUGE']))
print(main(['E', 'P4', 'ATS', 'ROUGE']))
