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
    a2, offset = parse(buffer, offset, 'double')
    a3, offset = parse(buffer, offset, 'double')
    a4, offset = parse(buffer, offset, 'uint16')
    a5, offset = parse(buffer, offset, 'uint64')
    a6, offset = parse(buffer, offset, 'int16')
    a7 = []
    for _ in range(2):
        e, offset = parse_e(buffer, offset)
        a7.append(e)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'uint32')
    b2, offset = parse(buffer, offset, 'uint32')
    b3, offset = parse_c(buffer, offset)
    b4, offset = parse(buffer, offset, 'uint64')
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'double')
    c2, offset = parse_d(buffer, offset)
    return {'C1': c1, 'C2': c2}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'double')
    d2, offset = parse(buffer, offset, 'float')
    d3 = []
    for _ in range(4):
        val, offset = parse(buffer, offset, 'uint16')
        d3.append(val)
    d4, offset = parse(buffer, offset, 'int64')
    d5, offset = parse(buffer, offset, 'uint64')
    d6, offset = parse(buffer, offset, 'int8')
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4, 'D5': d5,
            'D6': d6}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'uint16')
    e2, offset = parse(buffer, offset, 'uint8')
    e3 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint16')
        e3.append(val)
    e4 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint8')
        e4.append(val)
    e5, offset = parse(buffer, offset, 'int64')
    return {'E1': e1, 'E2': e2, 'E3': e3, 'E4': e4, 'E5': e5}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'ZRRQ\xd3\xe5\xda?\x86\xb2 3\xbb8\xb2\x1bK\x0b\xa2\xe6\xbfDP\x9d'
            b'\xdd\xb8\xb0\xdd\xbf\xd5PZ?Zh\xe4\xbc\xc1\x16\x86\xb9}\xe8\xb1\xdcz\xdfj'
            b"\x0b\x08\x11')FZtfQ\x88\x07\x95\xd7l<:\xf0\x88Q\xee\x9b\xcdp\xc9?\xe8\x94"
            b'{qF\x90\xd9\xbf\xd0\xab\xc7^\x05\xf8[\xfc\xc0\xcf\xf2\x036X7\x02\x00\x88'
            b'\x00\x00\x00\x02\x00\x8c\x00mu\xc6\xbeMOiep\x8b\x1e\x02\x00\x8e\x00\x00\x00'
            b'\x04\x00\x92\x00\x9bh\x0f@Y\xb9\xbc\xcd\xfb\x9d{Jy\x9c\xd6\x1f\xa0\x06(}Z<'))
