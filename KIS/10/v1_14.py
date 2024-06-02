def main(table):
    new_table = []
    trans = {'нет': '0', 'да': '1'}
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if string[1] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            yn = trans[string[1]]
            y, m, d = string[2].split('.')
            formated_date = f"{d}.{m}.{y[2:]}"
            mark = round(float(string[3].split('|')[1]), 1)
            formated_mark = str(float(mark))
            mail = string[3].split('|')[0].split('[')[0]
            new_table.append([yn, formated_date, formated_mark, mail])
    return new_table


data = [[None, 'нет', '2001.07.26', 'rusanz29[at]rambler.ru|0.5208'], [None, None, None, None],
        [None, None, None, None], [None, 'да', '1999.05.26', 'selevli62[at]rambler.ru|0.9866'],
        [None, 'нет', '2000.02.28', 'kasij58[at]yandex.ru|0.2509']]

from pprint import pprint
pprint(main(data))
