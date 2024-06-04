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
    a1, offset = parse(buffer, offset, 'int16')
    a2_offset, offset = parse(buffer, offset, 'uint32')
    a2, _ = parse_b(buffer, a2_offset)
    a3, offset = parse(buffer, offset, 'uint16')
    a4 = []
    for _ in range(7):
        val, offset = parse(buffer, offset, 'uint16')
        a4.append(val)
    a5 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int32')
        a5.append(val)
    a6, offset = parse(buffer, offset, 'int16')
    a7, offset = parse(buffer, offset, 'float')
    a8, offset = parse(buffer, offset, 'uint8')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7, 'A8': a8}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'int32')
    b2, offset = parse(buffer, offset, 'double')
    b3, offset = parse(buffer, offset, 'double')
    b4 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse_c(buffer, adr_offset)
        b4.append(val)
    b5_offset, offset = parse(buffer, offset, 'uint16')
    b5, _ = parse_d(buffer, b5_offset)
    b6, offset = parse_e(buffer, offset)
    b7, offset = parse(buffer, offset, 'float')
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4,
            'B5': b5, 'B6': b6, 'B7': b7}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'uint32')
    c2, offset = parse(buffer, offset, 'int32')
    c3, offset = parse(buffer, offset, 'int16')
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'uint32')
    d2 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int16')
        d2.append(val)
    d3, offset = parse(buffer, offset, 'uint32')
    return {'D1': d1, 'D2': d2,
            'D3': d3}, offset


def parse_e(buffer, offset):
    e1 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        e1.append(val)
    e2, offset = parse(buffer, offset, 'uint16')
    e3, offset = parse(buffer, offset, 'uint32')
    e4, offset = parse(buffer, offset, 'int16')
    e5, offset = parse(buffer, offset, 'uint64')
    e6, offset = parse(buffer, offset, 'int8')
    e7, offset = parse(buffer, offset, 'uint8')
    e8, offset = parse(buffer, offset, 'uint8')
    return {'E1': e1, 'E2': e2, 'E3': e3, 'E4': e4,
            'E5': e5, 'E6': e6, 'E7': e7, 'E8': e8}, offset


def main(data):
    result, _ = parse_a(data, 4)
    return result


data = (b'\xe0VZGN\x15\x00\x00\x00N\xa1u\xa8\xf2\xfeuu\xf0\xb0\x10\xa9\xd4\x11\xd6'
        b'#+\x00\x02\x00\x00\x00\x83\x8c[=)Sn!9\xc4\xa7@^\xb7\xd4\x1c\xc2\xf3!6\xbd'
        b'Ya/ 4b\xa7\xfa\x89\x90q\xab+\xe52\x00\x02\x00;\xe8\x07o\xcf\x04C=\xfaG'
        b"Y\x1b\xbf\xdaKW\x8e\xd5\x89H\xbf\xe0{\xdc]\x03\x7f\xf0\x00\x02\x00'\x00?"
        b"\x00\x03\x00K\xaf\x92\xf9g\xad\x96{6lw^'EIT&\xbb\xcf%=\x91,A\x80\xa5F\x9bk"
        b'\xdf\xc6=')

from pprint import pprint

pprint(main(data))
