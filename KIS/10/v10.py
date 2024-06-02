data = [["0.5371|Да", "03-06-02", "03-06-02"],
        ["0.7888|Да", "99-12-13", "99-12-13"],
        ["0.8762|Да", "00-07-14", "00-07-14"],
        ["0.2070|Нет", "02-01-21", "02-01-21"]]


def main(table):
    new_table = []
    unique_rows = set()
    slovar = {'да': 'Выполнено', 'нет': 'Не выполнено'}
    for string in table:
        row_tuple = tuple(string)
        if string[3] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            day, month, year = string[2].split('.')
            fdate = f"{year}-{month}-{day}"
            yon = slovar[string[3]]
            mail = string[4].split('[')[0]
            percent = str(int(float(string[5]) * 100)) + '%'
            new_table.append([fdate, yon, mail, percent])
    return new_table


from pprint import pprint

pprint(main(data))
