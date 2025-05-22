def main(x):
    x_4_top = {'QML': 1, 'LFE': 2, 'P4': 3}
    x_4_mid = {'QML': 4, 'LFE': 5, 'P4': 6}
    x_1 = {'MQL5': 9, 'PONY': 10, 'SLIM': 11}

    x_1_top = {'MQL5': 0, 'PONY': x_4_top[x[4]], 'SLIM': x_4_mid[x[4]]}
    x_0 = {2013: x_1[x[1]], 1982: 12}

    x3 = {1958: x_1_top[x[1]], 1965: 7, 1992: 8}
    x4 = {'QML': x_0[x[0]], 'LFE': 13, 'P4': 14}

    x2 = {1965: x3[x[3]],
          1961: x4[x[4]],
          2020: 15}
    return x2[x[2]]
