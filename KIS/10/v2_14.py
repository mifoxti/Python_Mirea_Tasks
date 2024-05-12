def main(table):
    new_table = []
    unique_rows = set()
    slon = {'false': '0', 'true': '1'}
    for string in table:
        row_tuple = tuple(string)
        if None not in string and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            name = row_tuple[0][5:]
            mail = row_tuple[1].split(']')[1]
            tF = slon[row_tuple[3]]
            new_table.append([name, mail, tF])
    return new_table


table = [
    ["Ф.М. Чичян", "cican68[at]yahoo.com", "cican68[at]yahoo.com", "false"],
    ["В.Ц. Мувелий", "muvelij23[at]yandex.ru", "muvelij23[at]yandex.ru", "true"],
    ["А.Д. Зотувев", "zotuvev24[at]yahoo.com", "zotuvev24[at]yahoo.com", "true"]
]

print(main(table))
