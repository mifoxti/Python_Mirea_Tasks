def main(fields):
    fields = [int(field) for field in fields]
    m1 = bin(int(fields[0]))[2:].zfill(2)
    m2 = bin(0)[2:].zfill(4)
    m3 = bin(int(fields[1]))[2:].zfill(3)
    m4 = bin(int(fields[2]))[2:].zfill(6)
    m5 = bin(int(fields[3]))[2:].zfill(1)
    return int(m5 + m4 + m3 + m2 + m1, 2)


print(main(('2', '2', '24', '1')))  # 45186
print(main(('1', '6', '39', '1')))  # 53121
print(main(('2', '0', '60', '1')))  # 63496
print(main(('0', '7', '16', '0')))  # 8640
