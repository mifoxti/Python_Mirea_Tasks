data = [[None, None, None, None], ['Выполнено', '0.2573', 'Святогор Б. Кифко', 'Святогор Б. Кифко'],
        ['Не выполнено', '0.1732', 'Альберт О. Цемедли', 'Альберт О. Цемедли'], [None, None, None, None],
        ['Не выполнено', '0.0341', 'Вадим У. Тукич', 'Вадим У. Тукич'],
        ['Не выполнено', '0.7928', 'Тимофей Д. Зицян', 'Тимофей Д. Зицян']]


def main(table):
    new_table = []
    unique_rows = set()
    slon = {'Выполнено': 'true', 'Не выполнено': 'false'}
    tf = []
    mark = []
    fio = []
    for string in table:
        row_tuple = tuple(string)
        if string[1] is not None and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            tf.append(slon[string[0]])
            mark.append("{:.0f}%".format(float(string[1]) * 100))
            parts = string[2].split()
            formatted_name = (parts[-1] + " " + parts[0][0] + "." +
                              parts[1][0] + ".")
            fio.append(formatted_name)
    new_table.append(tf)
    new_table.append(mark)
    new_table.append(fio)
    return new_table


from pprint import pprint

pprint(main(data))
