def main(x):
    dictx3_up = {2004: 0, 1973: 1}
    dictx0_m_up = {1958: 2, 2005: 3, 1971: 4}

    dictx1_mid = {'COOL': dictx3_up[x[3]],
                  'LLVM': dictx0_m_up[x[0]], 'PAWN': 5}

    dictx3_bot = {2004: 8, 1973: 9}

    dictx0_mid = {1958: 6, 2005: 7, 1971: dictx3_bot[x[3]]}

    dict_init = {'RAGEL': dictx1_mid[x[1]],
                 'IDL': dictx0_mid[x[0]], 'NSIS': 10}

    return dict_init[x[2]]


print(main([2005, 'COOL', 'NSIS', 2004]))  # = 10
