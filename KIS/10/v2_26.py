def main(table):
    mass = []
    unique_rows = set()
    slon = {'1': 'true', '0': 'false'}
    percents = []
    dates = []
    yn = []
    mails = []
    for string in table:
        row_tuple = tuple(string)
        if string[0] and row_tuple not in unique_rows:
            unique_rows.add(row_tuple)
            percent = str(float(string[0].rstrip('%')) / 100)
            percent = percent.ljust(5, '0')
            date, month, year = string[2].split('/')
            fdate = f"{year}/{month}/{date}"
            tof = slon[string[4]]
            mail = string[5].split('@')[1]
            percents.append(percent)
            dates.append(fdate)
            yn.append(tof)
            mails.append(mail)
    mass.append(percents)
    mass.append(dates)
    mass.append(yn)
    mass.append(mails)
    return mass


# Примеры таблиц
table1 = [
    ["85%", None, "13/03/03", None, "1", "turofberg57@gmail.com"],
    ["76%", None, "15/07/04", None, "1", "fotic47@mail.ru"],
    ["38%", None, "22/02/02", None, "0", "dikid83@mail.ru"],
    ["65%", None, "17/09/02", None, "1", "socutev52@yahoo.com"]
]

table2 = [
    ["47%", None, "26/09/04", None, "1", "mebij5@yahoo.com"],
    ["83%", None, "26/07/04", None, "1", "merak27@gmail.com"],
    ["54%", None, "23/12/03", None, "1", "secadin50@rambler.ru"],
    ["63%", None, "03/01/99", None, "1", "nosadan19@mail.ru"]
]

print(main(table1))
print(main(table2))
