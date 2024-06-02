def main(table):
    new_table = []
    marks = []
    dates = []
    names = []
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if string[1] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            mark = str(round(float(string[1]), 2)).ljust(5, '0')
            day, month, year = string[2].split('&')[0].split('-')
            fdate = f"{year[2::]}.{month}.{day}"
            name, fath, surn = string[2].split('&')[1].split(' ')
            fname = f"{name} {surn}"
            marks.append(mark)
            dates.append(fdate)
            names.append(fname)
    new_table.append(marks)
    new_table.append(dates)
    new_table.append(names)
    return new_table


data = [[None, '0.54', '28-04-1999&Тимур О. Кисянц'], [None, '0.60', '26-04-2002&Давид Ч. Вомогак'],
        [None, '0.31', '16-04-2004&Дмитрий Р. Гецафяк'], [None, '0.78', '04-04-2002&Арсен Ф. Фикий'],
        [None, '0.78', '04-04-2002&Арсен Ф. Фикий'], [None, '0.78', '04-04-2002&Арсен Ф. Фикий']]

from pprint import pprint

pprint(main(data))
