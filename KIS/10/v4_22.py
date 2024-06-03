def main(table):
    new_table = []
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if string[1] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            number, date = string[0].split('|')
            number = number.split(' ')[1]
            fnum = f"{number[:6]}-{number[6:]}"
            day, month, year = date.split('/')
            fdate = f"{year}-{month}-{day}"
            name, ini, fam = string[1].split(' ')
            fname = f"{name[0]}.{ini} {fam}"
            new_table.append([fdate, fnum, fname])
    return new_table


data = [['303 496-9565|20/01/00', 'Семен Е. Козий'], ['303 496-9565|20/01/00', 'Семен Е. Козий'],
        ['303 496-9565|20/01/00', 'Семен Е. Козий'], ['632 140-2028|22/05/00', 'Ильдар В. Цузулли'],
        ['891 327-6101|21/12/04', 'Данила М. Чуфянц']]

from pprint import pprint
pprint(main(data))
