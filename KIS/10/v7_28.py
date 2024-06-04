def main(table):
    new_table = []
    unique_rows = set()
    slon = {'Да': '1', 'Нет': '0'}
    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            name, fam = string[0].split(' ')
            fname = f"{name[:2]} {fam}"
            number = string[1].replace(' ', '').replace('-', '')
            day, month, year = string[2].split('.')
            fdate = f"{day}/{month}/{year[2:]}"
            yon = slon[string[3]]

            new_table.append([fname, number, fdate, yon])
    return new_table


data = [['А.А. Сонин', '+7 227 405-28-39', '23.06.2003', 'Да', None, '23.06.2003'],
        ['С.К. Чидарич', '+7 694 804-53-71', '23.04.2002', 'Нет', None, '23.04.2002'],
        ['Ф.Т. Лацев', '+7 564 937-74-04', '25.01.2002', 'Нет', None, '25.01.2002'],
        [None, None, None, None, None, None],
        ['Ф.Т. Лацев', '+7 564 937-74-04', '25.01.2002', 'Нет', None, '25.01.2002']]

from pprint import pprint

pprint(main(data))
