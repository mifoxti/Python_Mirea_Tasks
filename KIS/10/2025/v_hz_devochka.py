def main(table):
    new_table = []
    trans = {'Нет': 'N', 'Да': 'Y'}
    unique_rows = set()

    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            mail = string[0].split(']')[1]
            mark = f"{float(string[1]):.4f}"
            yon = trans[string[2].split('#')[0]]
            y, m, d = string[2].split('#')[1].split('.')
            fdate = f"{d}.{m}.{y[2::]}"
            new_table.append([mail, mark, yon, fdate])
    return new_table


data = [
    ['vasiliji[at]mail.ru', '0.31', 'Нет#2000.01.24'],
    ['andraeij[at]rambler.ru', '0.38', 'Да#2003.10.23'],
    ['veselov[at]gmail.com', '0.03', 'Нет#2013.02.12']
]

from pprint import pprint

pprint(main(data))
