def main(table):
    new_table = []
    name = []
    mail = []
    percents = []
    unique_rows = set()

    for string in table:
        row_tuple = tuple(string)
        if None not in string and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            f, i, o = string[1].split(';')[1].split(' ')
            form_name = f"{o}, {f[0]}.{i}"
            mark = round(float(string[0]), 2)
            formated_mark = str(float(mark)) + '0' * (4 - len(str(mark)))
            maile = string[1].split(';')[0].split('@')[0]
            percents.append(formated_mark)
            mail.append(maile)
            name.append(form_name)

    combined = list(zip(percents, mail, name))
    combined_sorted = sorted(combined, key=lambda x: x[1])
    percents_sorted, mail_sorted, name_sorted = zip(*combined_sorted)

    new_table.append(list(percents_sorted))
    new_table.append(list(mail_sorted))
    new_table.append(list(name_sorted))

    return new_table


data = [['0.380', 'ramil_61@yandex.ru;Рамиль Р. Шемин'],
        ['0.224', 'sevasman27@gmail.com;Валерий А. Севашман'],
        ['0.033', 'funogan54@yandex.ru;Марат Е. Фуногян']]
data2 = [['0.802', 'lalman6@yahoo.com;Тимур Б. Лалман'], ['0.001', 'ladberg12@gmail.com;Савва Ч. Ладберг'],
         ['0.997', 'timofej1@yahoo.com;Тимофей А. Мирян'], ['0.177', 'zizocak64@rambler.ru;Эмиль М. Цицочак']]
from pprint import pprint

pprint(main(data))
pprint(main(data2))
