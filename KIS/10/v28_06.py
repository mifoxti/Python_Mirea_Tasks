data = [
    ["Моравов Э.З.!moravov97[at]yahoo.com", "+7 338 209-75-55"],
    ["Текко И.В.!tekko17[at]mail.ru", "+7 690 671-11-85"],
    ["Шобагский Р.Ц.!sobagskij39[at]yahoo.com", "+7 537 190-87-84"],
    ["Кодеров П.Ц.!koderov17[at]rambler.ru", "+7 914 423-72-17"]
]


def main(table):
    new_table = []
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if None not in string and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            sur, name = string[0].partition("!")[0].split(" ")
            formated_name = f"{name[:2]} {sur}"
            mail = string[0].split("!")[1].split("]")[1]
            number = string[1].split(' ')
            formated_number = f"{number[0]} ({number[1]}) {number[2]}"
            new_table.append([mail, formated_number, formated_name])
    return new_table


from pprint import pprint

pprint(main(data))
