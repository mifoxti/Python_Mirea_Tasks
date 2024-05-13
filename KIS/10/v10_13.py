import re


def main(table):
    new_table = []
    unique_rows = set()
    mail = []
    marks = []
    yon = []
    for string in table:
        row_tuple = tuple(string)
        if string[0] is not None and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            mailname = string[0].split('[')[0]
            mark = str(round(float(string[2]), 1))
            tf = 'true' if string[4] == '1' else 'false'
            mail.append(mailname)
            marks.append(mark)
            yon.append(tf)
    new_table.append(mail)
    new_table.append(marks)
    new_table.append(yon)
    return new_table


data = [
    ["melak37[at]yahoo.com", None, "0.9629", None, "1"],
    ["gebotic86[at]gmail.com", None, "0.5281", None, "1"],
    ["rizanz85[at]yandex.ru", None, "0.3610", None, "0"],
    ["memuk68[at]mail.ru", None, "0.8604", None, "0"],
    ["memuk68[at]mail.ru", None, "0.8604", None, "0"]
]

from pprint import pprint

pprint(main(data))
