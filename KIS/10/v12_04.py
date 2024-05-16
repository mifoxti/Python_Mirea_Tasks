data = [
    [None, "Виктор Е. Зубов|+7 (954) 500-59-16", None, "0.611"],
    [None, "Вячеслав Г. Лирешман|+7 (011) 793-69-56", None, "0.062"],
    [None, "Филипп Ш. Чодли|+7 (867) 042-92-71", None, "0.711"],
    [None, "Ростислав Ф. Кавян|+7 (743) 204-38-25", None, "0.478"],
    [None, "Ростислав Ф. Кавян|+7 (743) 204-38-25", None, "0.478"]
]


def main(table):
    new_table = []
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if string[1] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            name, ini, fam = string[1].split('|')[0].split(' ')
            formated_name = f'{name} {fam}'
            number = string[1].split('|')[1].replace(' ', '')
            mark = ("{:.0f}%".format(float(string[3]) * 100))
            new_table.append([formated_name, number, mark])
    return new_table


from pprint import pprint

pprint(main(data))
