def main(table):
    new_table = []
    trans = {'1': 'Y', '0': 'N'}
    unique_rows = set()
    nums = []
    marks = []
    dates = []
    yons = []
    for string in table:
        row_tuple = tuple(string)
        if string[1] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            yn = trans[string[4]]
            y, m, d = string[3].split('/')
            formated_date = f"{d}-{m}-{y}"

            formated_mark = f"{round(float(string[1]), 3):.3f}"

            number = string[0].split(' ')[2].split('-')
            formated_number = f"{number[0]}-{number[1]}{number[2]}"

            nums.append(formated_number)
            marks.append(formated_mark)
            dates.append(formated_date)
            yons.append(yn)

    new_table.append(nums)
    new_table.append(marks)
    new_table.append(dates)
    new_table.append(yons)
    return new_table


if __name__ == '__main__':
    from pprint import pprint

    data = [
        ["+7 (104) 497-21-72", "0.5766", "2003/02/06", "2003/02/06", "1"],
        ["+7 (378) 732-68-44", "0.6628", "1999/10/06", "1999/10/06", "1"],
        ["+7 (274) 194-94-81", "0.5921", "2003/07/12", "2003/07/12", "0"],
        ["+7 (644) 100-35-86", "0.4899", "2000/05/03", "2000/05/03", "0"]
    ]
    pprint(main(data))
