def main(table):
    new_table = []
    unique_rows = set()
    for string in table:
        row_tuple = tuple(string)
        if None not in string and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            parts = string[0].split(":+")
            phone_number = (parts[1].replace(
                "(", "").replace(")", "")
                            .replace("-", "").replace(" ", "-"))
            date = parts[0].replace("/", ".")
            mark = str(round(float(string[2]), 2))
            if len(mark) < 4:
                mark += '0'
            new_row = [phone_number[2:9] + '-' + phone_number[9:], date,
                       mark]
            new_table.append(new_row)
    return new_table


input_table =[['01/11/03:+7 (436) 712-74-96', '0.547', '0.547'], ['08/02/01:+7 (949) 154-88-47', '0.498', '0.498'], ['01/11/03:+7 (436) 712-74-96', '0.547', '0.547'], ['01/11/03:+7 (436) 712-74-96', '0.547', '0.547'], ['05/03/01:+7 (222) 812-13-79', '0.816', '0.816'], ['26/10/02:+7 (861) 461-26-52', '0.789', '0.789']]
for row in main(input_table):
    print(row)
