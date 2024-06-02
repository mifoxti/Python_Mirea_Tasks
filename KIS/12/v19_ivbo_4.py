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
    offset = 3
    a1, offset = parse_b(buffer, offset)
    a2, offset = parse(buffer, offset, 'double')
    a3, offset = parse(buffer, offset, 'int8')
    a4, offset = parse(buffer, offset, 'int64')
    a5, offset = parse(buffer, offset, 'int8')
    a6, offset = parse(buffer, offset, 'uint16')
    a7, offset = parse(buffer, offset, 'int64')
    a8, offset = parse(buffer, offset, 'int8')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4, 'A5': a5,
            'A6': a6, 'A7': a7, 'A8': a8}, offset


def parse_b(buffer, offset):
    b1 = []
    for _ in range(2):
        a, offset = parse_c(buffer, offset)
        b1.append(a)
    b2, offset = parse(buffer, offset, 'float')
    b3, offset = parse_e(buffer, offset)
    return {'B1': b1, 'B2': b2, 'B3': b3}, offset


def parse_c(buffer, offset):
    c1_offset, offset = parse(buffer, offset, 'uint32')
    c1, _ = parse_d(buffer, c1_offset)
    c2, offset = parse(buffer, offset, 'uint16')
    c3 = []
    for _ in range(5):
        val, offset = parse(buffer, offset, 'uint8')
        c3.append(val)
    c4, offset = parse(buffer, offset, 'int16')
    c5, offset = parse(buffer, offset, 'int16')
    return {'C1': c1, 'C2': c2, 'C3': c3,
            'C4': c4, 'C5': c5}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'uint64')
    d2, offset = parse(buffer, offset, 'double')
    d3, offset = parse(buffer, offset, 'int8')
    d4, offset = parse(buffer, offset, 'uint32')
    d5, offset = parse(buffer, offset, 'int8')
    d6, offset = parse(buffer, offset, 'float')
    d7 = []
    for _ in range(5):
        val, offset = parse(buffer, offset, 'int16')
        d7.append(val)
    d8 = []
    for _ in range(8):
        val, offset = parse(buffer, offset, 'uint8')
        d8.append(val)
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4,
            'D5': d5, 'D6': d6, 'D7': d7, 'D8': d8}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'uint8')
    e2, offset = parse(buffer, offset, 'int16')
    e3, offset = parse(buffer, offset, 'int8')
    e4, offset = parse(buffer, offset, 'int64')
    return {'E1': e1, 'E2': e2, 'E3': e3, 'E4': e4}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


data = (b'DJPN\x00\x00\x00\xa9j\xdbH\xf7\x02\xfe\tW\xe10z\x00\x00\x00<\xfe\xfd\\\x84N'
        b'\x13\xa7\x7f\xd1\x98\xaa\x95\xce>\xc6\xbf\xee\xdb\t\xc6d\xc7R\xe0\r'
        b'\x1f:o\xca\x00r\xa7\xeb\xbfDZ\x1e\x06\x03\xf6\x87F\xaf\r\xd2\xab\r\xce\xeb'
        b'\x8b\xe0\xd3\x80\xc3|Ij\x05\x14*\xc6\xaa\xb6\xc4\x19\x1b\xeb\xe4I\xde?\xfdV'
        b'W\xb4\x8dm\x87\xe7\xb4\xbd5z\xa5\x99)d\xcfc\x18FY\xb4\x16\x8eI\x92'
        b'\xa6\x10\xa1l\xf1\xde\x87z\x02\xa5\xb0\xe9\x13\xd4\xc3\xcf\xb8?\xe3\x90Ml;C'
        b'M\x1c\x1f>\x9cDX\xb0\xee\xf97jJ~\xeb\xbf\xe0\xcb\xd8%\xa7A')
from pprint import pprint

pprint(main(data))
