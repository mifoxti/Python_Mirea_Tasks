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
    a1_offset, offset = parse(buffer, offset, 'uint32')
    a1, _ = parse_b(buffer, a1_offset)
    a2, offset = parse(buffer, offset, 'int16')
    a3, offset = parse(buffer, offset, 'double')
    a4 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse_c(buffer, adr_offset)
        a4.append(val)
    a5, offset = parse(buffer, offset, 'uint64')
    a6, offset = parse_d(buffer, offset)
    a7, offset = parse(buffer, offset, 'int32')
    a8, offset = parse(buffer, offset, 'int64')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4, 'A5': a5,
            'A6': a6, 'A7': a7, 'A8': a8}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'float')
    b2, offset = parse(buffer, offset, 'uint32')
    b3, offset = parse(buffer, offset, 'uint16')
    return {'B1': b1, 'B2': b2, 'B3': b3}, offset


def parse_c(buffer, offset):
    c1 = ''
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        c1 += (val.decode())
    c2, offset = parse(buffer, offset, 'int8')
    return {'C1': c1, 'C2': c2}, offset


def parse_d(buffer, offset):
    d1_offset, offset = parse(buffer, offset, 'uint16')
    d1, _ = parse_e(buffer, d1_offset)
    d2, offset = parse(buffer, offset, 'float')
    return {'D1': d1, 'D2': d2}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'int16')
    e2, offset = parse(buffer, offset, 'double')
    e3 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int16')
        e3.append(val)
    e4, offset = parse(buffer, offset, 'double')
    e5, offset = parse(buffer, offset, 'int16')
    e6, offset = parse(buffer, offset, 'double')
    e7 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'double')
        e7.append(val)
    return {'E1': e1, 'E2': e2, 'E3': e3, 'E4': e4,
            'E5': e5, 'E6': e6, 'E7': e7}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


data = (b'DSTC\x00\x00\x002.W\xbf\xc5;h!J\xa4 \x00\x00\x00\x02\x00A\x89\xe6(\x93'
        b"X@\x0c|\x00m>U\xd8~\xc6\x06C\xa3#\xc2=\xd2\xce\xbb\x05\xab\xbf\x16I'\xf0\xec"
        b'3\xf9\xc3Tpgiej\x00\x00\x00\x03\x00\x00\x00<*\x00\x00\x00\x02\x00\x00'
        b'\x00?\xcc\xeal\x10b}\xb9X\x9f\x19y?\xce\xfe\xda\xd9\x1e6(\xbf\xc3\x82'
        b']\xd8d\xec\xf0^\x8a?\xd4\x83\x9dl\xd0Y\xd8\x00\x05\x00\x00\x00S\xbf\xc5!'
        b'\xceU\t\xf3\x08\x9a\xe0?\xec8\x01\xd1~\xee\xba\x00\x00\x00\x02\x00]')
from pprint import pprint

pprint(main(data))
