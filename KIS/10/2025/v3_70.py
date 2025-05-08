def main(table):
    new_table = []
    years = []
    yons = []
    fios = []
    trans = {'Не выполнено': 'нет', 'Выполнено': 'да'}
    unique_rows = set()

    for string in table:
        row_tuple = tuple(string)
        if string[1] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            y, m, d = string[0].split('/')
            f_day = f"{y}"
            yon = trans[string[1].split('|')[0]]
            i, o, f = string[1].split('|')[1].split(' ')
            f_name = f"{f}, {i[0]}.{o}"
            years.append(f_day)
            yons.append(yon)
            fios.append(f_name)

    combined = list(zip(years, yons, fios))
    combined.sort(key=lambda x: x[2])
    sorted_years, sorted_yons, sorted_fios = zip(*combined)
    new_table.append(list(sorted_years))
    new_table.append(list(sorted_yons))
    new_table.append(list(sorted_fios))

    return new_table

from pprint import pprint
pprint(main([['2001/06/02', 'Не выполнено|Михаил У. Човичберг'], [None, None], [None, None], ['1999/05/18', 'Не выполнено|Георгий Ф. Мозак'], ['1999/01/22', 'Выполнено|Ярослав Б. Дофин']]))