def main(table):
    new_table = []
    unique_rows = set()
    slovar = {'Не выполнено': 'Нет', 'Выполнено': 'Да'}
    mails = []
    marks = []
    yons = []
    for row in table:
        row_tuple = tuple(row)
        if row[0] is not None and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            mail = row[0].replace('@', '[at]')
            mark = str(round(float(row[2]), 1))
            yon = slovar[row[3]]
            mails.append(mail)
            marks.append(mark)
            yons.append(yon)
    new_table.append(mails)
    new_table.append(marks)
    new_table.append(yons)
    return new_table
