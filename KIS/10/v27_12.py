data = [
    ["02.09.09:Да", "+7 931 092-35-56", "0.2299"],
    ["04.03.08:Да", "+7 507 543-28-70", "0.2445"],
    [None, None, None],  # добавлено в примере для учета пропусков
    ["02.12.08:Нет", "+7 798 130-52-19", "0.8578"],
    ["02.12.08:Нет", "+7 798 130-52-19", "0.8578"],
    ["02.12.08:Нет", "+7 798 130-52-19", "0.8578"]
]

def main(table):
    slovar = {'Да': 'true', 'Нет': 'false'}
    dates = []
    numbers = []
    tfki = []
    percents = []
    unique_rows = set()

    for string in table:
        if string[0] and string[1] and string[2]:
            row_tuple = tuple(string)
            if row_tuple not in unique_rows:
                unique_rows.add(row_tuple)
                date, yn = string[0].split(':')
                day, month, year = date.split('.')
                formated_date = f'{year}-{month}-{day}'
                phone_number = string[1]
                clean_number = (phone_number.replace("+7 ", "")
                                .replace(" ", "").replace("-", ""))
                area_code = clean_number[:3]
                first_part = clean_number[3:6]
                second_part = clean_number[6:]
                formatted_number = f"({area_code}) {first_part}-{second_part}"
                t_or_f = slovar[yn]
                percent = f"{float(string[2]) * 100:.0f}%"

                dates.append(formated_date)
                numbers.append(formatted_number)
                tfki.append(t_or_f)
                percents.append(percent)

    new_table = [dates, numbers, tfki, percents]
    return new_table

from pprint import pprint
pprint(main(data))
