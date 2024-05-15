data = [
    ["vsevolod72@gmail.com", '0.3399', '0.3399', "2003/10/24", "Всеволод И. Ноцотий"],
    ["cacimin81@yahoo.com", '0.3156', '0.3156', "2004/06/23", "Максим З. Чачимин"],
    ["marat71@yahoo.com", '0.4293', '0.4293', "1999/01/11", "Марат С. Гакак"]
]


def main(table):
    new_table = []
    unique_rows = set()
    slon = {'Выполнено': 'true', 'Не выполнено': 'false'}
    for string in table:
        row_tuple = tuple(string)
        if string[1] is not None and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            mail = string[0].replace('@', '[at]')
            date = string[3].replace('/', '-')
            name_sur = string[4].split()[2] + ' ' + string[4].split()[0]
            mark = ("{:.0f}%".format(float(string[1]) * 100))
            new_table.append([mail, mark, date, name_sur])
    return new_table


from pprint import pprint

pprint(main(data))
