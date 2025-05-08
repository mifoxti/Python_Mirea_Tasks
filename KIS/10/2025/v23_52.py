data = [
    ["", "fefuk87[at]yahoo.com", "1999.08.08", "", "фефук, Г.В.", "фефук, Г.В."],
    ["", "sisadberg42[at]mail.ru", "2001.10.03", "", "Шишадберг, М.О.", "Шишадберг, М.О."],
    ["", "retesko40[at]mail.ru", "1999.01.18", "", "Ретеско, В.С.", "Ретеско, В.С."]
]

data2 = [[None, 'fefuk87[at]yahoo.com', '1999.08.08', None, 'Фефук, Г.В.', 'Фефук, Г.В.'],
         [None, 'sisadberg42[at]mail.ru', '2001.10.03', None, 'Шишадберг, М.О.', 'Шишадберг, М.О.'],
         [None, 'retesko40[at]mail.ru', '1999.01.18', None, 'Ретеско, В.С.', 'Ретеско, В.С.']]


def main(table):
    new_table = []
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if string[1] and row_tuple not in unique_rows:
            mail = string[1].split('[at]')[1]
            y, m, d = string[2].split('.')
            f_day = f"{d}.{m}.{y[2::]}"
            f_name = string[4].replace(', ', ' ')[:-2].title()
            new_table.append([mail, f_day, f_name])
    return new_table


from pprint import pprint

pprint(main(data))
pprint(main(data2))