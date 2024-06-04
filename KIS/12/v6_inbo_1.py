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
    a1, offset = parse(buffer, offset, 'float')
    a2_offset, offset = parse(buffer, offset, 'uint16')
    a2, _ = parse_b(buffer, a2_offset)
    a3, offset = parse(buffer, offset, 'int16')
    return {'A1': a1, 'A2': a2, 'A3': a3}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'int64')
    b2, offset = parse(buffer, offset, 'uint32')
    b3, offset = parse_c(buffer, offset)
    b4, offset = parse(buffer, offset, 'uint8')
    b5, offset = parse(buffer, offset, 'int16')
    b6_offset, offset = parse(buffer, offset, 'uint32')
    b6, _ = parse_e(buffer, b6_offset)
    b7, offset = parse(buffer, offset, 'uint8')
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4,
            'B5': b5, 'B6': b6, 'B7': b7}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'double')
    c2 = []
    array_size, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_size):
        a3_offset, adr_offset = parse(buffer, adr_offset, 'uint32')
        val, _ = parse_d(buffer, a3_offset)
        c2.append(val)
    return {'C1': c1, 'C2': c2}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'uint16')
    d2, offset = parse(buffer, offset, 'int64')
    d3, offset = parse(buffer, offset, 'float')
    d4, offset = parse(buffer, offset, 'uint32')
    return {'D1': d1, 'D2': d2,
            'D3': d3, 'D4': d4}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'double')
    e2_offset, offset = parse(buffer, offset, 'uint16')
    e2, _ = parse_f(buffer, e2_offset)
    e3 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        e3.append(val)
    e4 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint32')
        e4.append(val)
    e5, offset = parse(buffer, offset, 'double')
    e6, offset = parse(buffer, offset, 'float')
    e7, offset = parse(buffer, offset, 'uint16')
    return {'E1': e1, 'E2': e2, 'E3': e3, 'E4': e4,
            'E5': e5, 'E6': e6, 'E7': e7}, offset


def parse_f(buffer, offset):
    f1, offset = parse(buffer, offset, 'int16')
    f2, offset = parse(buffer, offset, 'int64')
    f3, offset = parse(buffer, offset, 'int16')
    f4, offset = parse(buffer, offset, 'int8')
    f5, offset = parse(buffer, offset, 'uint32')
    f6, offset = parse(buffer, offset, 'int32')
    f7 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int16')
        f7.append(val)
    f8, offset = parse(buffer, offset, 'double')
    return {'F1': f1, 'F2': f2,
            'F3': f3, 'F4': f4,
            'F5': f5, 'F6': f6,
            'F7': f7, 'F8': f8}, offset


def main(data):
    result, _ = parse_a(data, 3)
    return result


data = (b'ZSIY\xfd\x1c?\x94\x00\x87\x95\xcceG\xcaq\xa7\x84\x1c\xd6^t\xca\x7f=\x93Z\x19'
        b'Jo\xf1\xf0r\xf0\xf0\x84Y\xa8Qf\xeb\xfe\xbeU\x02\xb9\xe3\x0b\x00\x00\x00\x1d'
        b'\x00\x00\x00\xdbyE\xa8\xfd\x8b\xfd\xfd5\xf6\x7f\xf5\x9d\xcc8]o\xa0\xcd4\xc8'
        b'\x10<\xd8\xcc\x9d\x92\x03\x007\x00\x00\x00\xf0wj\x02@\xc7\xb0?\x127+\xd5'
        b'-\xd8\xa3\x92z\x0bK\xe9/Ji\xf7\x93\xd60\xactH\xccK\xc5\xbf=\x00\x02\x00`\x00'
        b'\x04\x00\x00\x00b\x00*\xbb1\xae\x06\t\xe4\xbf\xd9\x9f\xd2\xbe\xae4\xa2l\xe0S'
        b':<\xf2P\xcd5\xeb0\xb2/+\xc3\xeeC\xe3\xbf\x02\x00/\x00\xee\x12Wr'
        b'\x00\x00\x00\xa9')
from pprint import pprint

pprint(main(data))
