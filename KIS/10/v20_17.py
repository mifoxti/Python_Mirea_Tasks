data = [
    ["00-07-22", None, "Ворерий Р.И.", "+7(098)108-87-49", "Ворерий Р.И."],
    ["04-11-21", None, "Лишук С.Ш.", "+7(150)925-92-89", "Лишук С.Ш."],
    ["02-12-21", None, "Гашев Г.М.", "+7(575)773-41-79", "Гашев Г.М."],
    ["00-07-22", None, "Ворерий Р.И.", "+7(098)108-87-49", "Ворерий Р.И."],
    ["00-03-08", None, "Кобетук Ф.Ш.", "+7(772)198-54-17", "Кобетук Ф.Ш."]
]


def main(table):
    unique_rows = set()
    names = []
    dates = []
    numbers = []
    for string in table:
        if string[0] and string[2]:
            row_tuple = tuple(string)
            if row_tuple not in unique_rows:
                unique_rows.add(row_tuple)
                on, tw, tr = string[0].split('-')
                formated_date = f'{tr}-{tw}-{on}'
                fam, name = string[2].split(' ')
                formated_name = f'{name[:2]} {fam}'
                phone_number = string[3]
                clean_number = phone_number.replace("+7(", "").replace(")", "")
                area_code = clean_number[:3]
                first_part = clean_number[3:6]
                second_part = clean_number[6:]
                formatted_number = f"{area_code} {first_part}-{second_part.replace('-', '')}"
                dates.append(formated_date)
                numbers.append(formatted_number)
                names.append(formated_name)
    new_table = [dates, names, numbers]
    return new_table


from pprint import pprint

pprint(main(data))
