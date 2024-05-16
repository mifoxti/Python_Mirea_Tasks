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
    a1, offset = parse(buffer, offset, 'int32')
    a2 = []
    array_size, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_size):
        a2_offset, adr_offset = parse(buffer, adr_offset, 'uint16')
        val, _ = parse_b(buffer, a2_offset)
        a2.append(val)
    a3_offset, offset = parse(buffer, offset, 'uint32')
    a3, _ = parse_c(buffer, a3_offset)
    a4, offset = parse(buffer, offset, 'uint32')
    a5, offset = parse(buffer, offset, 'uint8')
    a6, offset = parse(buffer, offset, 'int32')
    return {'A1': a1, 'A2': a2, 'A3': a3,
            'A4': a4, 'A5': a5, 'A6': a6}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'int64')
    b2, offset = parse(buffer, offset, 'double')
    b3, offset = parse(buffer, offset, 'uint8')
    return {'B1': b1, 'B2': b2, 'B3': b3}, offset


def parse_c(buffer, offset):
    c1 = ''
    for _ in range(6):
        val, offset = parse(buffer, offset, 'char')
        c1 += (val.decode())
    c2 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'float')
        c2.append(val)
    c3, offset = parse(buffer, offset, 'uint64')
    c4_offset, offset = parse(buffer, offset, 'uint16')
    c4, _ = parse_d(buffer, c4_offset)
    c5, offset = parse(buffer, offset, 'uint32')
    return {'C1': c1, 'C2': c2, 'C3': c3,
            'C4': c4, 'C5': c5}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'int16')
    d2 = []
    for _ in range(7):
        val, offset = parse(buffer, offset, 'float')
        d2.append(val)
    d3, offset = parse(buffer, offset, 'int8')
    return {'D1': d1, 'D2': d2, 'D3': d3}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


pprint(main(b'AHSF\xca\xeeE^^\x00\x03\x00\x00\x00O\x00\x00\x00\x84\x1a\xc5\xf5MF'
            b'\xb1\xeeO\x11\x9b%.\x8e\xaa\xb8\x9dY\xbf\xc4\\\x83H/\xbb\x88\x174.\xc8'
            b"Z_r\xe9\xd1?\xee^)\xa37D>u\xd5H\xdd'\x8d\x94\x04\x0e\xbf\xe3[\xbe\xfc\xa4"
            b'\xafl\xac\x00\x1c\x00-\x00>>\x0b\xba>\xbf9q\xfd>\x07j\x05>b\xedW\xae\x83>'
            b'\xc3\xe6\xbe<\x8f1\x95=\xb6i5\xbf_p\xd2\xbd\xcd\x92i?\x1f?\x8c\xbe'
            b'\xea\x80\x87\x0etsquwi\x00\x00\x00\x04\x00UT\xe2\xfe\xe3E\xf9#\xe9'
            b'\x00e\xb8\xca\xaf\x03'))
