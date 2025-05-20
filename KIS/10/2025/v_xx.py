def main(table):
    new_table = []
    unique_rows = set()
    trans = {'да': 'true', 'нет': 'false'}
    yons = []
    mails = []
    marks = []
    for string in table:
        row_tuple = tuple(string)
        if string[1] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            mail, yon = string[1].split(':')
            mark = float(string[3])

            mail = mail.split('[')[0]

            yon = trans[yon]

            mark = f"{round(float(mark), 3):.3f}"
            yons.append(yon)
            mails.append(mail)
            marks.append(mark)
    new_table.append(yons)
    new_table.append(mails)
    new_table.append(marks)
    return new_table
