def main(table):
    new_table = []
    unique_rows = set()
    slon = {'1': 'true', '0': 'false'}
    for string in table:
        row_tuple = tuple(string)
        if string[1] is not None and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            mark = str(round(float(string[1]), 1))
            yon = slon[string[3]]
            mail = string[4].split('[')[0]
            year, month, day = string[5].split('.')
            fdate = f"{day}.{month}.{year[2:]}"
            new_table.append([mark, yon, mail, fdate])
    return new_table


data = [[None, '0.134', None, '1', 'elisej66[at]yandex.ru', '2000.01.02'],
        [None, '0.580', None, '1', 'bimberg99[at]rambler.ru', '2002.08.22'],
        [None, '0.580', None, '1', 'bimberg99[at]rambler.ru', '2002.08.22'], [None, None, None, None, None, None],
        [None, '0.739', None, '0', 'stanislav95[at]gmail.com', '2002.02.18'],
        [None, '0.983', None, '1', 'fedor63[at]mail.ru', '2001.09.24']]
from pprint import pprint

pprint(main(data))
