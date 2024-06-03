from struct import *


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
    offset = 4
    a1_offset, offset = parse(buffer, offset, 'uint16')
    a1, _ = parse_b(buffer, a1_offset)
    a2, offset = parse(buffer, offset, 'uint16')
    return {'A1': a1, 'A2': a2}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'double')
    b2_offset, offset = parse(buffer, offset, 'uint16')
    b2, _ = parse_c(buffer, b2_offset)
    b3 = []
    array_size, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_size):
        a3_offset, adr_offset = parse(buffer, adr_offset, 'uint16')
        val, _ = parse_d(buffer, a3_offset)
        b3.append(val)
    b4_offset, offset = parse(buffer, offset, 'uint32')
    b4, _ = parse_e(buffer, b4_offset)
    b5, offset = parse(buffer, offset, 'int16')
    b6, offset = parse(buffer, offset, 'float')
    b7, offset = parse(buffer, offset, 'uint8')
    b8, offset = parse_f(buffer, offset)
    return {'B1': b1, 'B2': b2,
            'B3': b3, 'B4': b4,
            'B5': b5, 'B6': b6,
            'B7': b7, 'B8': b8}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'uint8')
    c2, offset = parse(buffer, offset, 'uint16')
    c3, offset = parse(buffer, offset, 'int32')
    c4, offset = parse(buffer, offset, 'uint64')
    c5 = ''
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        c5 += (val.decode())
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4,
            'C5': c5}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'int16')
    d2, offset = parse(buffer, offset, 'uint8')
    d3, offset = parse(buffer, offset, 'uint64')
    d4, offset = parse(buffer, offset, 'uint8')
    return {'D1': d1, 'D2': d2, 'D3': d3,
            'D4': d4}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'double')
    e2 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        e2.append(val)
    e3, offset = parse(buffer, offset, 'float')
    e4, offset = parse(buffer, offset, 'uint64')
    e5, offset = parse(buffer, offset, 'float')
    e6, offset = parse(buffer, offset, 'uint16')
    e7 = []
    for _ in range(7):
        val, offset = parse(buffer, offset, 'uint16')
        e7.append(val)
    return {'E1': e1, 'E2': e2,
            'E3': e3, 'E4': e4,
            'E5': e5, 'E6': e6,
            'E7': e7}, offset


def parse_f(buffer, offset):
    f1, offset = parse(buffer, offset, 'int16')
    f2 = []
    for _ in range(4):
        val, offset = parse(buffer, offset, 'double')
        f2.append(val)
    f3, offset = parse(buffer, offset, 'int64')
    return {'F1': f1, 'F2': f2,
            'F3': f3}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


data = (b'5GMTs\x00!ggmbwkc\x01o\xe1\x015e\xe9\xae\xd8\xdeI\x1cE\xc3o\x06\x00\x00'
        b'\x00\x08\x00\x00\x00!oJ\x7f\xeb\xb3\xb9u2\x9b\xce\xbb\x8a\x8eU'
        b"\xa0\x90\x98\xb7~\x016\x18\xcd%\x001\x00\xa2K\xbc'\xbc\xad?\xcc\xd9\xe6\xd7"
        b'\xbf\x04\x00\x00\x00A\x00(u\x0e\xbf\x05\xb1\xcc\xa0_\x0f\x0c\xee>'
        b'o\xf7\xbe\xef6\xbd\xbd\xdfI\x8b\xc9\xf7\xf8\x1f\xe3\xab\xe3\xb0\x00\xe0'
        b'\xf5\xc93\x88\xf3\xaa?\x0e\x00\x02\x00=\x00E\x00\x00\x00\xcco\xc9DQ\xbfe'
        b'$:\xf0\x817<\x1f\xfe\xb9\xbf\xb43a\x00N\xdd\xe3\xbf0vV\xed\xe18\xc2\xbf\xbc-'
        b'\xb0\x11d\xee\xdf\xbf\x15=\xcbR\x9d\x1e\x07F')

from pprint import pprint

pprint(main(data))
