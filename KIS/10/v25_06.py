table = [
    ["+7 147 479-5801", "cubamak3@yandex.ru&Семен К. Чубамяк", "+7 147 479-5801", "02-08-21"],
    ["+7 112 152-5149", "ignat27@yandex.ru&Игнат К. Сечий", "+7 112 152-5149", "00-07-28"],
    ["+7 147 479-5801", "cubamak3@yandex.ru&Семен К. Чубамяк", "+7 147 479-5801", "02-08-21"],
    ["+7 322 094-5010", "arsenij98@rambler.ru&Арсений Ф. Бамазин", "+7 322 094-5010", "04-11-10"],
    ["+7 147 479-5801", "cubamak3@yandex.ru&Семен К. Чубамяк", "+7 147 479-5801", "02-08-21"]
]

table2 = [
    ["+7 238 177-8641", "taserberg12@rambler.ru&Борис Ш. Тасерберг", "+7 238 177-8641", "00-02-06"],
    ["+7 088 876-8683", "zesifli31@yandex.ru&Радмир Л. Зесифли", "+7 088 876-8683", "00-04-04"],
    ["+7 088 876-8683", "zesifli31@yandex.ru&Радмир Л. Зесифли", "+7 088 876-8683", "00-04-04"],
    ["+7 614 009-4420", "nazar67@rambler.ru&Назар Т. Тодак", "+7 614 009-4420", "04-05-12"],
    ["+7 088 876-8683", "zesifli31@yandex.ru&Радмир Л. Зесифли", "+7 088 876-8683", "00-04-04"],
    ["+7 677 657-9499", "bucesak88@mail.ru&Леонид Ч. Бучесак", "+7 677 657-9499", "02-05-10"]
]


def main(table):
    new_table = []
    trans = {'Y': 'Выполнено', 'N': 'Не выполнено'}
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if None not in string and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            f_number = row_tuple[0][3:].replace(" ", "-")
            mail = row_tuple[1].split('&')[0].split('@')[0]
            full_name = row_tuple[1].split('&')[1]
            parts = full_name.split()
            last_name = parts[-1]
            initials = "".join(part[0] + "." for part in parts[:-1])
            formatted_name = f"{last_name} {initials}"
            somenum = '.'.join(row_tuple[3].split("-"))
            new_row = [f_number, formatted_name, somenum, mail]
            new_table.append(new_row)
    sorted_table = sorted(new_table, key=lambda x: x[3])
    return sorted_table


from pprint import pprint

pprint(main(table))
pprint(main(table2))
