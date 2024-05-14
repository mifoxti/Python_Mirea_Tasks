from struct import *


# РАБОТАЕТ
def parse(buffer, offset, type, order='<'):
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
    size = calcsize(order + pattern)
    value = unpack_from(order + pattern, buffer, offset)[0]
    return value, offset + size


def parse_a(buffer, offset):
    offset = 5
    a1, offset = parse_b(buffer, offset)
    a2_offset, offset = parse(buffer, offset, 'uint16')
    a2, _ = parse_d(buffer, a2_offset)
    a3_offset, offset = parse(buffer, offset, 'uint16')
    a3, _ = parse_e(buffer, a3_offset)
    a4, offset = parse_f(buffer, offset)
    a5, offset = parse(buffer, offset, 'int64')
    a6, offset = parse(buffer, offset, 'int64')
    a7, offset = parse(buffer, offset, 'float')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'float')
    b2 = ''
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        b2_char, adr_offset = parse(buffer, adr_offset, 'char')
        b2 += b2_char.decode()
    b3, offset = parse(buffer, offset, 'int8')
    b4 = []
    for _ in range(4):
        e, offset = parse_c(buffer, offset)
        b4.append(e)
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'int8')
    c2, offset = parse(buffer, offset, 'int64')
    c3, offset = parse(buffer, offset, 'int8')
    c4, offset = parse(buffer, offset, 'uint8')
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'int64')
    d2 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int16')
        d2.append(val)
    return {'D1': d1, 'D2': d2}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'uint8')
    e2, offset = parse(buffer, offset, 'uint32')
    e3 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'float')
        e3.append(val)
    e4, offset = parse(buffer, offset, 'int16')
    e5, offset = parse(buffer, offset, 'double')
    e6, offset = parse(buffer, offset, 'int32')
    e7, offset = parse(buffer, offset, 'int32')
    return {'E1': e1, 'E2': e2, 'E3': e3, 'E4': e4, 'E5': e5,
            'E6': e6, 'E7': e7}, offset


def parse_f(buffer, offset):
    f1, offset = parse(buffer, offset, 'float')
    f2 = []
    for _ in range(7):
        val, offset = parse(buffer, offset, 'uint16')
        f2.append(val)
    return {'F1': f1, 'F2': f2}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'KVGU\x03RM=>\x02\x00\x00\x00h\x00\x00\x00\xfd\r\xa1\x0b\x9e\x9de\x058r\xe0'
            b'pL-\x95\xad\xb4\xc9p\x1d\x0cTSE\xe8\xbc\x89F|\xb4#}*\xa5\xce\xe2{\xdeT'
            b'\xceF\r\xc8\xca\x00n\x00\x82\x00Xc\xe2>\xbdt\x88[!\x93\xc6N\xc4-\x19Ed\xa8'
            b"(\x02\xb0\xf2\x17\xfcA]\xae6'\xd7\xd1\x85\xf7\r\x87\xeb\x92;ji>\xcb"
            b'$\xa0\xba\x81~\x04\xa4Q\xf9L\x02\x00j\x00O_I\xbf9\x9a\t\xbd\x0f\xa8'
            b'\x8c\xae:\x02\x00z\x00\x00\x00\xa0<\x14\x12\x06\x8b\xa6R\xee?\xd9\xe5Y\xe1;'
            b'b\x08#'))
