from pprint import pprint
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
    a2, offset = parse(buffer, offset, 'uint32')
    a3, offset = parse(buffer, offset, 'uint64')
    return {'A1': a1, 'A2': a2, 'A3': a3}, offset


def parse_b(buffer, offset):
    b1 = []
    for _ in range(3):
        val, offset = parse_c(buffer, offset)
        b1.append(val)
    b2 = []
    for _ in range(5):
        val, offset = parse(buffer, offset, 'int16')
        b2.append(val)
    b3, offset = parse(buffer, offset, 'int16')
    b4, offset = parse(buffer, offset, 'float')
    b5 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint16')
        b5.append(val)

    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4, 'B5': b5}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'int16')
    c2 = []
    for _ in range(7):
        val, offset = parse(buffer, offset, 'uint16')
        c2.append(val)
    c3_offset, offset = parse(buffer, offset, "uint32")
    c3, _ = parse_d(buffer, c3_offset)
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'int16')
    d2 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int16')
        d2.append(val)
    return {'D1': d1, 'D2': d2}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


pprint(main(b'BIBS\xe6\xfc\x19\xf7\xe6B\x10+<\xa3\x80\xd8_\x8b\xe3)8g\x00\x00\x00\\w\xda'
            b'O\xb1\x1a\xe3_/CW\xd3\x10!\x9f\xe5u\x00\x00\x00[@\\\xdd\xbf\x99\x04E\nV?'
            b'\xaf5\xa9\xec\xc6\x85\x00\x00\x00\xc7\xa1"\x02ls\xf2Ii\x8a\x99\xd9\xc5\x15t'
            b'?\x02\x00\x8f\x00\x00\x00\x1c&q\xff\x86\xd73\x8a\x9f\xed\xfe\xea\xa2'
            b'\xf2\xc1\x8a3\x08\x02\x00\x00\x00c\x00\x00\x00\x00~q\x82v\xce\x02'
            b'\x00\x00\x00q\x00\x00\x00\xf3p\x89$_\x0e\xf0\x83\x03\x00\x00\x00\x7f'
            b'\x00\x00\x00\xfc\x0b|\xe1'))
