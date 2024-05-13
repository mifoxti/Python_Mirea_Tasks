from pprint import pprint
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
    a1, offset = parse_b(buffer, offset)
    a2, offset = parse(buffer, offset, 'uint8')
    a3, offset = parse(buffer, offset, 'uint16')
    a4_offset, offset = parse(buffer, offset, 'uint32')
    a4, _ = parse_c(buffer, a4_offset)
    a5, offset = parse(buffer, offset, 'uint8')
    a6, offset = parse(buffer, offset, 'float')
    a7, offset = parse(buffer, offset, 'float')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'double')
    b2, offset = parse(buffer, offset, 'int8')
    b3, offset = parse(buffer, offset, 'float')
    b4, offset = parse(buffer, offset, 'int16')
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'int64')
    c2_offset, offset = parse(buffer, offset, 'uint16')
    c2, _ = parse_d(buffer, c2_offset)
    c3, offset = parse(buffer, offset, 'uint8')
    c4 = []
    for _ in range(2):
        val, offset = parse(buffer, offset, 'uint64')
        c4.append(val)
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4}, offset


def parse_d(buffer, offset):
    b3size, offset = parse(buffer, offset, 'uint32')
    b3offs, offset = parse(buffer, offset, 'uint16')
    d1 = []
    for _ in range(b3size):
        val, b3offs = parse_e(buffer, b3offs)
        d1.append(val)
    d2_offset, offset = parse(buffer, offset, 'uint16')
    d2, _ = parse_f(buffer, d2_offset)
    d3, offset = parse(buffer, offset, 'uint8')
    return {'D1': d1, 'D2': d2, 'D3': d3}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'int8')
    e2, offset = parse(buffer, offset, 'uint32')
    e3, offset = parse(buffer, offset, 'uint16')
    e4, offset = parse(buffer, offset, 'uint32')
    e5 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        e5.append(val)
    return {'E1': e1, 'E2': e2, 'E3': e3, 'E4': e4, 'E5': e5}, offset


def parse_f(buffer, offset):
    f1 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        f1.append(val)
    f2, offset = parse(buffer, offset, 'int32')
    f3, offset = parse(buffer, offset, 'int16')
    f4, offset = parse(buffer, offset, 'uint16')
    return {'F1': f1, 'F2': f2, 'F3': f3, 'F4': f4}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


pprint(main(b'\xdeXHFG?\xec\x97qjK\xba\x10\xc3\xbfX\x93\xeaH#\xf4\xa5Q\x00\x00\x00z\xd4'
            b'?\x03,\xb4\xbf \x87\xealN\xc7_\x19\x9a\x1es\x84\x15I\xaf\x8c\xf2VA'
            b'\xcf\xa1\xe7m\x00\x00\x00\x04\x00$\xdf\xf5m\x9a\xc8\xed\xf43\xbd7'
            b'\xb4\x00\x00\x00\x03\x00(\xd0\x1a\xb3\xec\xf7=}\\\xec\xc3$\x00\x00'
            b'\x00\x02\x00+U\xba0\x00\x00\x00\x03\x00`\xf0\x9b\xd9\xbb\xfc:%'
            b'\xad\x00\x00\x00\x03\x00-\x00c0p\xd3aA\x80\xed\x1a\x07\x00q\x8c\x14\x9aH'
            b'1O\xaa1\xf8$\xff\xeb\x9b\xfa;\xe5\xe8'))
