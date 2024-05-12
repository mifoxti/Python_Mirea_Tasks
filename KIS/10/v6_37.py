import re


def main(table):
    new_table = []
    unique_rows = set()
    slon = {'да': 'true', 'нет': 'false'}
    phone = []
    dates = []
    yon = []
    mail = []
    for string in table:
        row_tuple = tuple(string)
        if string[1] is not None and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            phone_number = row_tuple[0]
            formatted_number = re.sub(r'\+(\d+)\((\d+)\)(\d+)-(\d+)-(\d+)',
                                      r'(\2) \3-\4-\5', phone_number)
            date_string = row_tuple[1].split('!')[0]
            day, month, year = date_string.split('/')
            formatted_date = f"{year}.{month}.{day}"
            yn = slon[row_tuple[1].split('!')[1]]
            mail1 = row_tuple[2].split(']')[1]
            phone.append(formatted_number)
            dates.append(formatted_date)
            yon.append(yn)
            mail.append(mail1)
    new_table.append(phone)
    new_table.append(dates)
    new_table.append(yon)
    new_table.append(mail)
    return new_table


table = [
    ["+7(128)432-30-13", "21/01/2003!да", "tovan21[at]yahoo.com"],
    ["+7(822)205-33-13", "25/02/1999!да", "bukov71[at]yahoo.com"],
    ["+7(414)092-73-64", "16/02/2000!да", "tadisov12[at]yandex.ru"],
    ["+7(414)092-73-64", "16/02/2000!да", "tadisov12[at]yandex.ru"],
    ["+7(414)092-73-64", "16/02/2000!да", "tadisov12[at]yandex.ru"]
]
from pprint import pprint

pprint(main(table))
