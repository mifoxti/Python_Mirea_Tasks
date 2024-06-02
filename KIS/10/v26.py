def main(table):
    new_table = []
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            name = string[0].split(' ')[1]
            day, month, year = string[1].split('-')
            fdate = f"{year}/{month}/{day}"
            yon = "Y" if string[3] == 'Да' else "N"
            new_table.append([name, fdate, yon])
    return new_table


data = [['Вячеслав Нубич', '22-11-2002', '22-11-2002', 'Да'], ['Василий Тусобич', '17-03-2003', '17-03-2003', 'Да'],
        ['Василий Тусобич', '17-03-2003', '17-03-2003', 'Да'], ['Арсений Бешовли', '05-01-2002', '05-01-2002', 'Да'],
        ['Анатолий Рамко', '02-07-2000', '02-07-2000', 'Да']]

from pprint import pprint

pprint(main(data))
