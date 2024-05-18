def main(table):
    new_table = []
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if string[0] is not None and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            mark, mail = string[0].split(';')
            mark = mark + '0'
            mail = mail.split(']')[1]
            date = string[3].replace('/', '.')
            name, fam = string[4].split(' ')
            form_name = f"{name[0:2]} {fam}"
            new_table.append([mail, date, mark, form_name])
    return new_table


data = [
    ["0.50;zosimak28[at]rambler.ru", None, None, "2000/06/14", "П.М. Цосимак"],
    ["0.21;gelokskij24[at]mail.ru", None, None, "2004/08/13", "А.О. Гелокский"],
    ["0.91;cinuk18[at]yandex.ru", None, None, "2001/08/12", "В.Р. Чинук"],
    ["0.91;cinuk18[at]yandex.ru", None, None, "2001/08/12", "В.Р. Чинук"]
]
