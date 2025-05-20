def main(table):
    new_table = []
    unique_rows = set()
    trans = {'да': '1', 'нет': '0'}
    yons = []
    mails = []
    marks = []
    for string in table:
        row_tuple = tuple(string)
        if string[2] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            yon, mark = string[2].split('#')

            mail = string[3].split('@')[0]

            yon = trans[yon]

            mark = f"{round(float(mark), 2):.2f}"
            yons.append(yon)
            marks.append(mark)
            mails.append(mail)
    new_table.append(yons)
    new_table.append(marks)
    new_table.append(mails)
    return new_table


from pprint import pprint

data = [[None, None, 'да#0.650', 'kazuk90@rambler.ru', 'kazuk90@rambler.ru'],
        [None, None, 'да#0.265', 'mofuzov12@yandex.ru', 'mofuzov12@yandex.ru'],
        [None, None, 'да#0.271', 'zuzozic15@gmail.com', 'zuzozic15@gmail.com'],
        [None, None, 'нет#0.740', 'ledanz8@mail.ru', 'ledanz8@mail.ru'],
        [None, None, 'нет#0.740', 'ledanz8@mail.ru', 'ledanz8@mail.ru']]
pprint(main(data))
