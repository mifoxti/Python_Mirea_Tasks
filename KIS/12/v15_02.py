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
    a1_offset, offset = parse(buffer, offset, 'uint32')
    a1, _ = parse_b(buffer, a1_offset)
    a2, offset = parse(buffer, offset, 'int32')
    a3, offset = parse(buffer, offset, 'uint64')
    a4, offset = parse(buffer, offset, 'int32')
    a5, offset = parse(buffer, offset, 'uint64')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4, 'A5': a5}, offset


def parse_b(buffer, offset):
    b1_offset, offset = parse(buffer, offset, 'uint16')
    b1, _ = parse_c(buffer, b1_offset)
    b2, offset = parse(buffer, offset, 'float')
    b3 = []
    for _ in range(2):
        e, offset = parse_d(buffer, offset)
        b3.append(e)
    b4, offset = parse(buffer, offset, 'float')
    b5, offset = parse(buffer, offset, 'uint32')
    b6, offset = parse(buffer, offset, 'uint8')
    b7 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'float')
        b7.append(val)
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4,
            'B5': b5, 'B6': b6, 'B7': b7}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'uint8')
    c2 = ''
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        c2 += (val.decode())
    c3, offset = parse(buffer, offset, 'int64')
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'float')
    d2, offset = parse(buffer, offset, 'int64')
    d3, offset = parse(buffer, offset, 'uint16')
    d4, offset = parse(buffer, offset, 'uint16')
    d5, offset = parse(buffer, offset, 'int64')
    d6 = []
    for _ in range(5):
        val, offset = parse(buffer, offset, 'uint8')
        d6.append(val)
    return {'D1': d1, 'D2': d2, 'D3': d3,
            'D4': d4, 'D5': d5, 'D6': d6}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


pprint(main(b'\xe6HULRA\x00\x00\x00\xf1y\xb9\xd2e/C\xf9\xf18v\xa1f+e\xbc\x9d\xcfu'
 b'\xe4\x85\x8bv\x0elfi\x10\x03\x00\x00\x00!\x00\x00\x00\r{\xf6h O\x1e'
 b'\x99\xfa\x16\x1b\xbf\x9d\xa7>?\xf2\xb7C\xbf$\x00\x01\xc3\xf1=\xc1\x07~\xbe>'
 b'\x1ad\xab_\xa7)2\xa9\x03<\x0e\xa75\xf9\xc0*\xceF\x99\x9c{;%=[\xebH\xbf'
 b'(\xb4\xfb\xa4\xa5\xa3\xdcf#\xf7\xac@\xa6zoE\xeb}\xd0k\x97wi\xa4'
 b'\xb1\x9d\xd8\x9b\xbe\x08t+\x7f\x02\x03\x00\x00\x005\x00\x00\x00'))
