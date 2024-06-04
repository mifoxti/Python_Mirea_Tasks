def main(table):
    new_table = []
    unique_rows = set()
    slon = {'true': 'Y', 'false': 'N'}
    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            yon, mail = string[0].split('#')
            yon = slon[yon]
            mail = mail.split('@')[0]
            mark = f"{round(float(string[1]) * 100)}%"

            new_table.append([mail, yon, mark])
    return new_table


data = [
    ['false#viktor36@yahoo.com', '0.385'],
    ['false#georgij42@yahoo.com', '0.179'],
    ['true#razikak81@yahoo.com', '0.905']
]

from pprint import pprint

pprint(main(data))
