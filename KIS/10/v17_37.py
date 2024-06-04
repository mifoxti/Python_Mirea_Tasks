import re


def main(table):
    new_table = []
    unique_rows = set()
    slon = {'N': '0', 'Y': '1'}
    for string in table:
        row_tuple = tuple(string)
        if string[1] is not None and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            yon, mail = string[1].split('&')
            yon = slon[yon]
            mail = mail.replace('[at]', '@')
            number = string[2][:3] + " " + string[2][4:]
            name, fam = string[3].split(' ')
            fname = f"{name[:2]} {fam}"
            new_table.append([yon, number, mail, fname])
    return new_table

string = '006-560-6457'
number = string[:3] + " " + string[4:]
string = 'М.М. Гумугко'
name, fam = string.split(' ')
fname = f"{name[:2]} {fam}"
print(fname)