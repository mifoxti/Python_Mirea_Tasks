def main(table):
    new_table = []
    marks = []
    mails = []
    dates = []
    unique_rows = set()

    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            mark = f"{round(float(string[0]) * 100)}%"
            mail = string[1].replace('[at]', '@')
            y, m, d = string[2].split('-')
            f_date = f"{d}/{m}/{y}"
            marks.append(mark)
            mails.append(mail)
            dates.append(f_date)
    new_table.append(marks)
    new_table.append(mails)
    new_table.append(dates)
    return new_table


data = [['0.4', 'sifosko11[at]gmail.com', '2002-12-02'], [None, None, None], ['0.4', 'sifosko11[at]gmail.com', '2002-12-02'], [None, None, None], ['0.4', 'sifosko11[at]gmail.com', '2002-12-02'], ['0.1', 'lusuk92[at]yahoo.com', '1999-03-06'], ['0.5', 'bazov31[at]yandex.ru', '2004-01-25'], ['0.2', 'lizefin12[at]yahoo.com', '1999-11-02']]

from pprint import pprint
pprint(main(data))