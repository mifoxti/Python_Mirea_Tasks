data = [
    ['3635658486:21.07.02', 'N', 'N'],
    ['8075852178:26.03.02', 'N', 'N'],
    ['4812995841:01.01.03', 'N', 'N']
]


def main(table):
    new_table = []
    trans = {'Y': 'Выполнено', 'N': 'Не выполнено'}
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if None not in string and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            data = row_tuple[0].split(':')
            snils = data[0]
            form_snils = f"{snils[:3]} {snils[3:6]}-{snils[6:]}"
            form_date = '-'.join(data[1].split('.'))
            y_or_n = trans[row_tuple[1]]
            new_row = [form_snils, form_date, y_or_n]
            new_table.append(new_row)
    return new_table

from pprint import pprint
pprint(main(data))
