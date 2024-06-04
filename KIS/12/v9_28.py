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
    a1, offset = parse(buffer, offset, 'int16')
    a2, offset = parse(buffer, offset, 'int32')
    a3 = ''
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        a3 += (val.decode())
    a4 = ''
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        a4 += (val.decode())
    a5, offset = parse_b(buffer, offset)
    a6 = []
    array_size, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_size):
        a3_offset, adr_offset = parse(buffer, adr_offset, 'uint16')
        val, _ = parse_d(buffer, a3_offset)
        a6.append(val)
    a7, offset = parse_e(buffer, offset)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'uint8')
    b2, offset = parse(buffer, offset, 'double')
    b3, offset = parse_c(buffer, offset)
    return {'B1': b1, 'B2': b2, 'B3': b3}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'uint8')
    c2, offset = parse(buffer, offset, 'float')
    c3, offset = parse(buffer, offset, 'uint32')
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset


def parse_d(buffer, offset):
    d1 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        d1.append(val)
    d2, offset = parse(buffer, offset, 'int16')
    d3, offset = parse(buffer, offset, 'float')
    return {'D1': d1, 'D2': d2, 'D3': d3}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'uint16')
    e2, offset = parse(buffer, offset, 'float')
    e3, offset = parse(buffer, offset, 'uint32')
    e4, offset = parse(buffer, offset, 'double')
    e5, offset = parse(buffer, offset, 'uint32')
    return {'E1': e1, 'E2': e2, 'E3': e3, 'E4': e4,
            'E5': e5}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


data = (b'\x0fZQG}D\xc5\xf8\xa8\xa9\x00\x00\x00\x03\x00B\x00\x05\x00E\x0e\xbf\xcf '
        b'\xec<G\x96\xd0b>v\xf5\t)\x9c\xd84\x00\x00\x00\x04\x00\x7ff\x16\xbf7'
        b'\xf2\xd3\x03\xf2\xf3 \xbf\xee|\xa2P\xe9d\xa4\x979\xd7\x96qymaykfu1\xbe'
        b'\x00\x02\x00Jpc\xbd\xd5\x01u\xcd\xf5\xe2\x00\x03\x00VC\xdc\xbf'
        b'\x13\x7f\xb8\xdd\xe7\x87\xdd\x00\x04\x00c\xcaj?O\x08\x9c\xa9\xbb\x08'
        b'@\x00\x04\x00q\\M\xbfpk3\x00L\x00Y\x00g\x00u')
from pprint import pprint

pprint(main(data))
