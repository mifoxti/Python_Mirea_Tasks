def main(table):
    new_table = []
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            mail = string[0].split('@')[1]
            fam, mark = string[3].split('#')
            fam = fam.split()[0]
            mark = str(round(float(mark), 1))
            new_table.append([mail, mark, fam])
    return sorted(new_table, key=lambda x: x[2])


data = [[None, None, None, None], [None, None, None, None],
        ['bifosberg84@rambler.ru', None, 'bifosberg84@rambler.ru', 'Бифосберг Ростислав#0.07'],
        ['vucasidi30@mail.ru', None, 'vucasidi30@mail.ru', 'Вучашиди Роман#0.45'],
        ['radmir9@yahoo.com', None, 'radmir9@yahoo.com', 'Цидов Радмир#0.64']]

from pprint import pprint

pprint(main(data))
