data = [
    ["17.03.02", "kamodij42[at]yahoo.com|51%", "Петр В. Камодий", "17.03.02"],
    ["02.09.03", "mihail10[at]gmail.com|39%", "Михаил И. Гудич", "02.09.03"],
    ["14.07.01", "tamerlan82[at]gmail.com|38%", "Тамерлан В. Нигиди", "14.07.01"],
    ["09.05.02", "platon65[at]yahoo.com|30%", "Платон Е. Вифян", "09.05.02"]
]


def main(table):
    new_table = []
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if string[0] is not None and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            day, month, year = string[0].split('.')
            form_date = f"{year}-{month}-{day}"
            mail = string[1].split('|')[0].split(']')[1]
            mark = string[1].split('|')[1].rstrip('%')
            new_mark = f"0.{mark}00" if len(mark) > 1 else f"0.0{mark}00"
            name, ini, fam = string[2].split(' ')
            form_name = f"{fam} {name}"
            new_table.append([form_date, new_mark, mail, form_name])
    return new_table


data2 = [
    ["27.12.04", "sosman40[at]rambler.ru|28%", "Ян Ч. Сосман", "27.12.04"],
    ["21.08.03", "kolic24[at]mail.ru|7%", "Егор Ч. Колич", "21.08.03"],
    ["08.10.01", "vufutko33[at]gmail.com|41%", "Борис Е. Вуфутко", "08.10.01"],
    ["22.12.02", "zobafan29[at]rambler.ru|21%", "Данила Е. Цобафян", "22.12.02"]
]

from pprint import pprint

pprint(main(data))
pprint(main(data2))
