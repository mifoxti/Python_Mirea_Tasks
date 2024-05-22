data = [
    ["tusanz5[at]yahoo.com", "Юрий У. Тушянц", "нет|02.07.01", "Юрий У. Тушянц"],
    ["tusanz5[at]yahoo.com", "Юрий У. Тушянц", "нет|02.07.01", "Юрий У. Тушянц"],
    ["gelefidi2[at]yandex.ru", "Данил Л. Гелефиди", "нет|01.07.15", "Данил Л. Гелефиди"],
    ["tamerlan81[at]yahoo.com", "Тамерлан С. Регянц", "нет|03.05.24", "Тамерлан С. Регянц"]
]


def main(table):
    new_table = []
    unique_rows = set()
    slon = {'нет': '0', 'да': '1'}
    for string in table:
        row_tuple = tuple(string)
        if string[1] is not None and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            mail = string[0].split('[')[0]
            f, i, o = string[1].split(' ')
            formated_name = f'{f[:1]}.{i} {o}'
            zerone = slon[string[2].split('|')[0]]
            d, m, y = string[2].split('|')[1].split('.')
            formated_date = f"{y}-{m}-{d}"
            new_table.append([mail, formated_name, zerone, formated_date])
    return new_table


from pprint import pprint

pprint(main(data))
