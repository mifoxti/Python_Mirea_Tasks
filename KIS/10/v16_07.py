data = [["0.5371|Да", "03-06-02", "03-06-02"],
        ["0.7888|Да", "99-12-13", "99-12-13"],
        ["0.8762|Да", "00-07-14", "00-07-14"],
        ["0.2070|Нет", "02-01-21", "02-01-21"]]


def main(table):
    new_table = []
    unique_rows = set()
    slovar = {'Да': 'Выполнено', 'Нет': 'Не выполнено'}
    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            mark = str(round(float(string[0].split('|')[0]), 1))
            your = slovar[string[0].split('|')[1]]
            y, m, d = string[2].split('-')
            formated_date = f"{d}.{m}.{y}"
            new_table.append([mark, your, formated_date])
    return new_table


from pprint import pprint

pprint(main(data))
