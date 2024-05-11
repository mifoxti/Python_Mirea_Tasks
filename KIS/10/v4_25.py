import math


def main(table):
    new_table = []
    unique_rows = set()
    slon = {'Не выполнено': 'нет', 'Выполнено': 'да'}
    names = []
    yens = []
    numbers = []
    for string in table:
        row_tuple = tuple(string)
        if None not in string and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            number = row_tuple[0]
            formated_id = number[:6] + number[7:]
            yN = slon[row_tuple[1]]
            mark = str(round(float(row_tuple[2]), 2))
            if len(mark) < 4:
                mark += '0'
            names.append(formated_id)
            yens.append(yN)
            numbers.append(mark)
    new_table.append(names)
    new_table.append(yens)
    new_table.append(numbers)
    return new_table


data = [
    ["018-50-37", "Не выполнено", 0.4609],
    [None, None, None],
    ["483-41-15", "Выполнено", 0.2882],
    ["945-94-60", "Выполнено", 0.3101],
    ["142-83-94", "Не выполнено", 0.5518]
]

from pprint import pprint

pprint(main(data))
