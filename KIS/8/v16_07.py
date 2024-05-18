def main(bit_fields):
    fields = [int(field) for field in bit_fields]
    q1 = bin(int(fields[0]))[2:].zfill(3)
    q2 = bin(int(fields[1]))[2:].zfill(1)
    q3 = bin(int(fields[2]))[2:].zfill(7)
    q4 = bin(int(fields[3]))[2:].zfill(6)
    result = str(hex(int(q4 + q3 + q2 + q1, 2)))
    return result


# Test cases
print(main(('4', '1', '56', '28')))  # Output: '0xe38c'
print(main(('3', '1', '35', '32')))  # Output: '0x102b'
print(main(('5', '0', '43', '59')))  # Output: '0x1dab5'
print(main(('0', '1', '3', '34')))  # Output: '0x1038'
