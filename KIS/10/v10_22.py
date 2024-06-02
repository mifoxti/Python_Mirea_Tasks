data = [
    ["0.8!1", "fuguk21[at]gmail.com", "fuguk21[at]gmail.com"],
    ["0.7!0", "duzibin9[at]yahoo.com", "duzibin9[at]yahoo.com"],
    ["0.5!0", "sofij39[at]mail.ru", "sofij39[at]mail.ru"],
    ["0.7!0", "duzibin9[at]yahoo.com", "duzibin9[at]yahoo.com"]
]


def main(table):
    new_table = []
    unique_rows = set()
    slovar = {'1': 'Y', '0': 'N'}
    yN = []
    mail = []
    mark = []
    for row in table:
        row_tuple = tuple(row)
        if row[0] is not None and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            yN.append(slovar[row_tuple[0].split('!')[1]])
            mail.append(row_tuple[1].replace('[at]', '@'))
            mark.append(row_tuple[0].split('!')[0] + '00')
    new_table.append(yN)
    new_table.append(mail)
    new_table.append(mark)
    return new_table


from pprint import pprint
pprint(main(data))