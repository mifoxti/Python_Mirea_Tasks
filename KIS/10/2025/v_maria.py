def main(table):
    new_table = []
    unique_rows = set()
    trans = {'true': 'Да', 'false': 'Нет'}
    nums = []
    yons = []
    mails = []
    for string in table:
        row_tuple = tuple(string)
        if string[1] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            num, yon = string[1].split('&')
            f_num = num.replace('-', '')

            yon = trans[yon]

            mail = string[3].replace('@', '[at]')

            nums.append(f_num)
            yons.append(yon)
            mails.append(mail)
    new_table.append(nums)
    new_table.append(yons)
    new_table.append(mails)
    return new_table


from pprint import pprint

data = [[None, '857-9953&true', None, 'viktor83@yandex.ru', 'viktor83@yandex.ru'],
        [None, '862-1864&false', None, 'danil61@yandex.ru', 'danil61@yandex.ru'], [None, None, None, None, None],
        [None, '393-2731&false', None, 'kitirskij41@rambler.ru', 'kitirskij41@rambler.ru'],
        [None, '393-2731&false', None, 'kitirskij41@rambler.ru', 'kitirskij41@rambler.ru']]
pprint(main(data))
