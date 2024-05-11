from struct import *


# РАБОТАЕТ
def parse(buffer, offset, type, order='>'):
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
    a1, offset = parse(buffer, offset, 'int32')
    a2, offset = parse(buffer, offset, 'int64')
    a3, offset = parse(buffer, offset, 'int16')
    a4, offset = parse_b(buffer, offset)
    a5, offset = parse_d(buffer, offset)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4, 'A5': a5}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'uint16')
    b2 = []
    for _ in range(5):
        b2_offset, offset = parse(buffer, offset, 'uint16')
        val, _ = parse_c(buffer, b2_offset)
        b2.append(val)
    b3, offset = parse(buffer, offset, 'int16')
    b4, offset = parse(buffer, offset, 'double')
    b5, offset = parse(buffer, offset, 'float')
    b6 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint8')
        b6.append(val)
    b7 = []
    for _ in range(2):
        val, offset = parse(buffer, offset, 'int64')
        b7.append(val)
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4, 'B5': b5,
            'B6': b6, 'B7': b7}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'int64')
    c2 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int16')
        c2.append(val)
    return {'C1': c1, 'C2': c2}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'uint64')
    d2, offset = parse(buffer, offset, 'uint8')
    d3, offset = parse(buffer, offset, 'uint64')
    d4, offset = parse(buffer, offset, 'int32')
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'\xc9BCOL\xe1\xd8\xc2\xbd\xd6m\xfc\xcb\x01\x1a7\xbb\xdb\xe5\x98\xb8\x00^\x00'
            b't\x00\x86\x00\x9a\x00\xb0a\xbb?\xe3\x9e\xcd*\xc5\x90D>\xa3\xda\r\x00\x00\x00'
            b'\x02\x00\x00\x00\xbe\x8a\x98\xa1\x93&\x1fI\x1d19\x1e\xdd\x8eA\xf2'
            b"\xd5'\x85\x1f\x9c\x9bsf\x83f\xa0\x88H\x99\xf1\xdd\xcc\xd0\x17\xe8"
            b'\xa1\xd8\xe5\xa8\x0c\xef\xdb\x08\x9e\xab\x84F\x8b\xd9\x00\x00\x00\x02\x00Z'
            b'd\x10\xd4\x9aN\x8f\x0fY\x10@Ve\xcd\x1b`\xcb\x00\x00\x00\x04\x00l\x9ea'
            b'\x12\x15@\xf4\x16\xb8A\xb96\xdb\x00\x00\x00\x02\x00\x82\xfb4\xb8i'
            b'\xc9\x96\xb0\xe3w@\x17\xbc\xf5\xb7\x00\x00\x00\x03\x00\x94Y\xab\xaf.'
            b'\xdd\xf2\xb5o\x13\xf7\xf0\xe9\xd6q\x1d\x95\x00\x00\x00\x04\x00\xa8\xd6\xb2'))
