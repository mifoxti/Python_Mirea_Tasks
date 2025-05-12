def main(table):
    new_table = []
    names = []
    dates = []
    yons = []
    trans = {'0': 'N', '1': 'Y'}
    unique_rows = set()

    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            i, o, f = string[0].split(' ')
            names.append(f"{f} {i}")

            y, m, d = string[1].split('.')
            dates.append(f"{y[2::]}/{m}/{d}")

            yons.append(trans[string[4]])

    new_table.append(names)
    new_table.append(dates)
    new_table.append(yons)
    return new_table


data = [[None, None, None, None, None], ['Георгий Б. Цанянц', '2000.07.20', '2000.07.20', None, '0'],
        ['Ильдар О. Шифич', '2000.10.01', '2000.10.01', None, '1'],
        ['Тихон Ф. Цобян', '2002.05.12', '2002.05.12', None, '0']]
from pprint import pprint

pprint(main(data))
