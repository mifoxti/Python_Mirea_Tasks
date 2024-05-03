from struct import *

# РАБОТАЕТ
def parse(buffer, offset, type):
    pattern = {
        'float': 'f',
        'double': 'd',
        'char': 'c',
        'int8': 'b',
        'uint8': 'B',
        'int16': 'h',
        'uint16': 'H',
        'int32': 'i',
        'uint32': 'I',
        'int64': 'q',
        'uint64': 'Q'
    }[type]
    size = calcsize(type)
    value = unpack_from(type, buffer, offset)[0]
    return value.decode() if type[-1] in 's' else value, offset + size


def parse_a(buffer, offset):
    a1, offset = parse(buffer, offset, '<4s')
    a2, offset = parse(buffer, offset, '<b')
    a3, offset = parse(buffer, offset, '<q')
    a4 = []
    for _ in range(3):
        a4_offset, offset = parse(buffer, offset, '<I')
        val, _ = parse_b(buffer, a4_offset)
        a4.append(val)
    a5, offset = parse_d(buffer, offset)
    a6_offset, offset = parse(buffer, offset, "<H")
    a6, offset = parse_e(buffer, a6_offset)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4, 'A5': a5, 'A6': a6}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, '<b')
    b2, offset = parse_c(buffer, offset)
    return {'B1': b1, 'B2': b2}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, '<b')
    c2, offset = parse(buffer, offset, '<b')
    c3 = []
    array_size, offset = parse(buffer, offset, '<I')
    adr_offset, offset = parse(buffer, offset, '<I')
    for _ in range(array_size):
        val, adr_offset = parse(buffer, adr_offset, '<H')
        c3.append(val)
    c4, offset = parse(buffer, offset, '<I')
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, '<B')
    d2, offset = parse(buffer, offset, '<H')
    return {'D1': d1, 'D2': d2}, offset


def parse_e(buffer, offset):
    e1 = []
    array_size, offset = parse(buffer, offset, '<I')
    adr_offset, offset = parse(buffer, offset, '<I')
    for _ in range(array_size):
        val, adr_offset = parse(buffer, adr_offset, '<I')
        e1.append(val)
    e2, offset = parse(buffer, offset, '<f')
    return {'E1': e1, 'E2': e2}, offset


def main(data):
    result, _ = parse_a(data, 4)
    return result


data1 = (b'COUpgrvv\x85j&\t\xdcZ\xb0\xc6\xb9&\x00\x00\x009\x00\x00\x00L\x00\x00'
         b'\x00\xd9\xac\xa3o\x00\xb2&\xc6{\x16o\xd7\x02\x00\x00\x00"\x00\x00'
         b'\x00,\xa9\x8e~h\xe7540H\xf0\x02\x00\x00\x005\x00\x00\x00e$\xba\xb9\x061@\x97'
         b':\x18\x06\x02\x00\x00\x00H\x00\x00\x00\x9d\x96\xa7\x03\xc7\xdb~\x92\x05'
         b"$\x92\x97\x0fl\x14\xb1\x956'\xe9\xe3<\x8ah\x05\x00\x00\x00[\x00\x00\x00\x84"
         b'DU?')

result1 = main(data1)
print(result1)
for i in main(data1):
    print(i, ":", result1[i])
