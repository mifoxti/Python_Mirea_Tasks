data = [
    [None, "04.05.2004", "0.36:Y", "Герман Н. Зурицак", "Герман Н. Зурицак"],
    [None, "06.10.2004", "0.92:Y", "Святослав С. Рицецов", "Святослав С. Рицецов"],
    [None, "20.05.2004", "0.35:Y", "Кирилл Ф. Батянц", "Кирилл Ф. Батянц"],
    [None, "26.09.2002", "0.07:Y", "Игорь З. Кезорук", "Игорь З. Кезорук"]
]


def main(table):
    new_table = []
    unique_rows = set()
    slon = {'N': 'нет', 'Y': 'да'}
    for string in table:
        row_tuple = tuple(string)
        if string[1] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            date, month, year = string[1].split('.')
            form_date = f'{year}.{month}.{date}'
            mark = string[2].split(':')[0] + '00'
            yN = slon[string[2].split(':')[1]]
            name, ini, fam = string[3].split(' ')
            form_name = f'{fam}, {name[0]}.{ini}'
            new_table.append([form_date, yN, form_name, mark])
    return new_table


from pprint import pprint

pprint(main(data))
