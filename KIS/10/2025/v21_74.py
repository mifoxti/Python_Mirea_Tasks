def main(table):
    new_table = []
    unique_rows = set()
    trans = {'true': '1', 'false': '0'}
    for string in table:
        row_tuple = tuple(string)
        if string[1] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            yon, data = string[0].split('|')
            mail = string[1].replace('[at]', '@')
            mark = f"0.{string[2].rstrip('%')}0"
            d, m, y = data.split('.')
            f_date = f"{y}/{m}/{d}"
            yon = trans[yon]
            new_table.append([f_date, mail, mark, yon])
    return new_table
