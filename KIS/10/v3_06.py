data = [
    ["+7 (755) 867-92-61", "1999-02-21", "Рамиль З. Нецин", "ramil_38[at]yahoo.com", "ramil_38[at]yahoo.com"],
    ["+7 (354) 832-02-44", "2002-03-12", "Герман И. Фефафиди", "fefafidi51[at]yahoo.com", "fefafidi51[at]yahoo.com"],
    ["+7 (681) 125-89-73", "2001-02-12", "Артур О. Димубук", "dimubuk60[at]yandex.ru", "dimubuk60[at]yandex.ru"]
]


def main(table):
    unique_rows = set()
    names = []
    dates = []
    numbers = []
    mails = []
    for string in table:
        if string[0] and string[2]:
            row_tuple = tuple(string)
            if row_tuple not in unique_rows:
                unique_rows.add(row_tuple)
                phone_number = string[0]
                clean_number = phone_number.replace("+7 ", "")
                formated_number = clean_number[:12] + clean_number[13:]
                y, m, d = string[1].split("-")
                formated_date = f"{d}-{m}-{y[2:]}"
                name, ini, fam = string[2].split(" ")
                formated_name = f"{fam} {name}"
                mail = string[3].split('[')[0]
                numbers.append(formated_number)
                dates.append(formated_date)
                names.append(formated_name)
                mails.append(mail)
    new_table = [numbers, dates, names, mails]
    return new_table


from pprint import pprint

pprint(main(data))
