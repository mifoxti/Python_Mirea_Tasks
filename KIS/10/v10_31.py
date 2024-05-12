import math


def main(table):
    new_table = []
    unique_rows = set()
    slon = {'Не выполнено': '0', 'Выполнено': '1'}
    dates = []
    yens = []
    numbers = []
    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)

            number = row_tuple[0].split('&')[0]
            formated_number = (number.replace('(', '')
                               .replace(')', '').replace('-', ''))
            dat = row_tuple[0].split('&')[1]
            day, month, year = dat.split('-')
            formatted_date = f"{year}.{month}.{day}"
            yN = slon[row_tuple[2]]
            dates.append(formatted_date)
            yens.append(yN)
            numbers.append(formated_number)
    new_table.append(dates)
    new_table.append(yens)
    new_table.append(numbers)
    sorted_indices = sorted(range(len(new_table[2])),
                            key=lambda x: new_table[2][x])
    sorted_table = [[row[i] for i in sorted_indices] for row in new_table]
    return sorted_table


data = [
    ["+7(052)122-60-34&18-02-2002", None, "Выполнено"],
    ["+7(125)409-84-71&05-05-2001", None, "Выполнено"],
    ["+7(149)400-67-09&11-12-2001", None, "Не выполнено"],
    ["+7(755)750-33-81&24-10-2002", None, "Выполнено"]
]

from pprint import pprint

pprint(main(data))
