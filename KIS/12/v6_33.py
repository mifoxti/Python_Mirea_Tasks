from struct import *


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
    a1, offset = parse(buffer, offset, 'int8')
    a2, offset = parse(buffer, offset, 'float')
    a3 = ''
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        a3 += (val.decode())
    a4 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse_b(buffer, adr_offset)
        a4.append(val)
    a5, offset = parse(buffer, offset, 'int8')
    a6_offset, offset = parse(buffer, offset, 'uint16')
    a6, _ = parse_c(buffer, a6_offset)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4, 'A5': a5,
            'A6': a6}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'uint16')
    b2, offset = parse(buffer, offset, 'double')
    return {'B1': b1, 'B2': b2}, offset


def parse_c(buffer, offset):
    c1_offset, offset = parse(buffer, offset, 'uint16')
    c1, _ = parse_d(buffer, c1_offset)
    c2_offset, offset = parse(buffer, offset, 'uint16')
    c2, _ = parse_e(buffer, c2_offset)
    c3, offset = parse(buffer, offset, 'uint8')
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'int8')
    d2, offset = parse(buffer, offset, 'uint32')
    d3, offset = parse(buffer, offset, 'uint16')
    return {'D1': d1, 'D2': d2, 'D3': d3}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'uint32')
    e2, offset = parse(buffer, offset, 'float')
    e3, offset = parse(buffer, offset, 'double')
    e4, offset = parse(buffer, offset, 'int32')
    e5, offset = parse(buffer, offset, 'int64')
    e6 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        e6.append(val)
    e7 = []
    for _ in range(7):
        val, offset = parse(buffer, offset, 'uint8')
        e7.append(val)
    e8, offset = parse(buffer, offset, 'uint16')
    return {'E1': e1, 'E2': e2, 'E3': e3, 'E4': e4,
            'E5': e5, 'E6': e6, 'E7': e7, 'E8': e8}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


data = (b'\x06QLVY+=,/r\x00\x02\x00\x17\x00\x02\x00\x00\x00\x19(\x00`bb\x12\xa0?'
        b'\xe4\x1e(F\xea\xabtg\xfd\xbf\xea\x90\xf8r\x11\xc0\x98=\x05\xa2n\xe1\xc9\xdf'
        b'\x1a\xdc\x88\x80iXm\xbd_\x14\xed?\xb5>~\x8aV\x0c\xc0\x86B\x88w\xf4'
        b'\x00\xb6\xcd*\xcdg3\x00\x03\x004\x1b\xd7p\x89\xa7h=\xca7\x00-\x007E')
from pprint import pprint

pprint(main(data))
