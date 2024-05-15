data = [
    [None, "Готедин Савелий:(863) 597-1318", 0.577, None, 0.577],
    [None, "Геков Юрий:(836) 680-4664", 0.359, None, 0.359],
    [None, "Тобосов Амир:(218) 859-0551", 0.953, None, 0.953],
    [None, "Тобосов Амир:(218) 859-0551", 0.953, None, 0.953],
    [None, "Мачский Всеволод:(332) 166-5535", 0.787, None, 0.787]
]


def main(table):
    new_table = []
    unique_rows = set()
    marks = []
    names = []
    numbers = []
    for string in table:
        row_tuple = tuple(string)
        if string[1] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            name = string[1].split(':')[0].split(' ')[0]
            number = (string[1].split(':')[1].replace('(', '')
                      .replace(')', '').replace(' ', '').replace('-', ''))
            mark = str(round(float(string[2]), 1))
            marks.append(mark)
            names.append(name)
            numbers.append(number)
    new_table.append(numbers)
    new_table.append(names)
    new_table.append(marks)
    sorted_indices = sorted(range(len(new_table[0])),
                            key=lambda x: new_table[0][x])
    sorted_table = [[row[i] for i in sorted_indices] for row in new_table]
    return sorted_table


from pprint import pprint

pprint(main(data))
