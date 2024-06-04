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
    offset = 4
    a1, offset = parse(buffer, offset, 'uint8')
    a2 = []
    for _ in range(7):
        a, offset = parse_b(buffer, offset)
        a2.append(a)
    a3, offset = parse(buffer, offset, 'uint32')
    a4, offset = parse_c(buffer, offset)
    a5, offset = parse(buffer, offset, 'int32')
    a6, offset = parse(buffer, offset, 'float')
    a7, offset = parse(buffer, offset, 'double')
    a8, offset = parse(buffer, offset, 'int8')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7, 'A8': a8}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'int16')
    b2, offset = parse(buffer, offset, 'uint16')
    b3 = ''
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        b3 += (val.decode())
    return {'B1': b1, 'B2': b2, 'B3': b3}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'int32')
    c2, offset = parse(buffer, offset, 'uint8')
    c3, offset = parse(buffer, offset, 'int64')
    c4, offset = parse(buffer, offset, 'uint16')
    c5, offset = parse(buffer, offset, 'uint16')
    c6, offset = parse_d(buffer, offset)
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4,
            'C5': c5, 'C6': c6}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'int64')
    d2, offset = parse(buffer, offset, 'int64')
    d3, offset = parse(buffer, offset, 'uint16')
    d4, offset = parse(buffer, offset, 'uint8')
    d5 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int64')
        d5.append(val)
    d6 = []
    for _ in range(6):
        val, offset = parse(buffer, offset, 'float')
        d6.append(val)
    d7, offset = parse(buffer, offset, 'float')
    d8, offset = parse(buffer, offset, 'int64')
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4,
            'D5': d5, 'D6': d6, 'D7': d7, 'D8': d8}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


data = (b'NDUC\xa3J\xf5\xe6D\x00\x00\x00\x02\x00\x00\x00\xbc\xcd\xb8E\xae\x00\x00\x00'
        b'\x02\x00\x00\x00\xbes\xb2N\x99\x00\x00\x00\x02\x00\x00\x00\xc0\xe1\xcd\x92'
        b'\x9d\x00\x00\x00\x02\x00\x00\x00\xc2\xa59\x1c\xbe\x00\x00\x00'
        b'\x02\x00\x00\x00\xc4`\x81H\x85\x00\x00\x00\x02\x00\x00\x00\xc6\xe2\x0c\x92'
        b'\xc9\x00\x00\x00\x02\x00\x00\x00\xc8\xa9t\xfa\xc0r\x9d\x9e\x9f\xc0\x16\xeb'
        b'y\xf2\x99\xef@H\xc8\xde~`\x8at-\xfb;\x02\xdb\xcd\x0f[\xf6\xa0\x06\x14'
        b'\xefe\r\xb1\x01\x00\x00\x00\x02\x00\xca\xbfP\xcb\xf1=\xf7u\xa7\xbc'
        b'\x84\xd3\xff>=*\x9e>\xb0w\x8d><\xc5G>\xf0\xbd\x85g\xd7?k\x12G\x0e\x960'
        b'\xa6\xd2\x1c?H\xb2x\xbf\xef\xde\xf3}\x82\xac\xb2pfyoooxvehgbkwn}='
        b"\xfa\x8d\\\xce\xac\xe9\x17\xd4't\xc3Sq\xb0")

from pprint import pprint

pprint(main(data))
