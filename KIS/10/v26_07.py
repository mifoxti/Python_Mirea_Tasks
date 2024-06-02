def main(table):
    new_table = []
    unique_rows = set()
    dates = []
    marks = []
    fams = []
    numbers = []
    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            d, m, y = string[0].split(';')[0].split('/')
            number = string[0].split(';')[1].replace('(', '').replace(')', '')
            mark = string[3] + '0' * (6 - len(string[3]))
            fam = string[4][:-5]
            dates.append(f'{y}/{m}/{d}')
            marks.append(mark)
            fams.append(fam)
            numbers.append(number)
    new_table.append(dates)
    new_table.append(marks)
    new_table.append(fams)
    new_table.append(numbers)
    return new_table


data = [['13/07/1999;+7 (271) 180-22-65', None, None, '0.873', 'Рекский М.Р.'],
        ['13/12/2004;+7 (369) 395-97-08', None, None, '0.547', 'Кусазук В.И.'],
        ['12/11/2000;+7 (372) 476-09-70', None, None, '0.555', 'Рутберг Д.Л.'],
        ['12/11/2000;+7 (372) 476-09-70', None, None, '0.555', 'Рутберг Д.Л.'],
        ['06/02/2001;+7 (030) 220-18-88', None, None, '0.041', 'Луфовский А.Е.']]


from pprint import pprint
pprint(main(data))
