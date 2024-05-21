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
    a1 = ''
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        a1 += (val.decode())
    a2, offset = parse(buffer, offset, 'double')
    a3_offset, offset = parse(buffer, offset, 'uint16')
    a3, _ = parse_b(buffer, a3_offset)
    a4, offset = parse(buffer, offset, 'int16')
    a5_offset, offset = parse(buffer, offset, 'uint32')
    a5, _ = parse_d(buffer, a5_offset)
    a6_offset, offset = parse(buffer, offset, 'uint16')
    a6, _ = parse_e(buffer, a6_offset)
    a7, offset = parse(buffer, offset, 'int64')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7}, offset


def parse_b(buffer, offset):
    b1 = []
    for _ in range(3):
        c_offset, offset = parse(buffer, offset, 'uint32')
        c, _ = parse_c(buffer, c_offset)
        b1.append(c)
    b2 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint16')
        b2.append(val)
    return {'B1': b1, 'B2': b2}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'uint16')
    c2, offset = parse(buffer, offset, 'uint64')
    return {'C1': c1, 'C2': c2}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'int64')
    d2, offset = parse(buffer, offset, 'uint64')
    d3, offset = parse(buffer, offset, 'double')
    d4 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint32')
        d4.append(val)
    d5, offset = parse(buffer, offset, 'int64')
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4,
            'D5': d5}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'int64')
    e2, offset = parse(buffer, offset, 'uint8')
    e3, offset = parse(buffer, offset, 'double')
    e4, offset = parse(buffer, offset, 'int32')
    e5, offset = parse(buffer, offset, 'float')
    e6, offset = parse(buffer, offset, 'uint16')
    return {'E1': e1, 'E2': e2, 'E3': e3,
            'E4': e4, 'E5': e5, 'E6': e6}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


pprint(main(b'SQON\x8d\x00\x03\x00\x00\x00%\xbf\xb2\x17uT\xe4\xba@\x00L\xd9\x97\x00'
            b'\x00\x00h\x00\x90\xe3\x9a2\xde,\x1d\x8fQatf\xe8\x932H\xe5\x00X"\x98l\xc1\x92'
            b'\x0bs\x01\x98\xd6\xe7\xc7\\\xb7o6o\xc0\x89l"4lt\xa0\xb64U.\x00\x00\x00('
            b'\x00\x00\x002\x00\x00\x00<\x00\x03\x00FG\x91N\xe8\xed\xdd\xd7l\xfdt\x95v'
            b'H\x0f\x10\x0e?\xc1y\xa65\xe3?\xa0\xbeg3\x1a?\xedV9\xcbz\xe1\x80'
            b'\x00\x00\x00\x03\x00\x00\x00\\Wcs\xb1B\x90\xc3\xfd6rL\xb6\xac49\x86'
            b'\xf9\xbf\xe3S\xae\xdcx,\xe2\x80\xe1\xab\xd6?G\tL\xf8\xa4'))
