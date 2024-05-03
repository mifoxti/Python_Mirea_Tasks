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
    a1, offset = parse(buffer, offset, 'uint16')
    a2, offset = parse(buffer, offset, 'int32')
    a3, offset = parse(buffer, offset, 'uint16')
    a4, offset = parse(buffer, offset, 'uint16')
    a5_offset, offset = parse(buffer, offset, 'uint16')
    a5, _ = parse_b(buffer, a5_offset)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4, 'A5': a5}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'uint8')
    b2, offset = parse(buffer, offset, 'float')
    b3 = []
    array_size, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_size):
        b3_offset, adr_offset = parse(buffer, adr_offset, 'uint16')
        val, _ = parse_c(buffer, b3_offset)
        b3.append(val)
    b4_offset, offset = parse(buffer, offset, 'uint16')
    b4, _ = parse_d(buffer, b4_offset)
    b5, offset = parse(buffer, offset, 'double')
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4, 'B5': b5}, offset


def parse_c(buffer, offset):
    c1 = []
    for _ in range(6):
        val, offset = parse(buffer, offset, 'uint32')
        c1.append(val)
    c2, offset = parse(buffer, offset, 'uint8')
    return {'C1': c1, 'C2': c2}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'float')
    d2 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        d2.append(val)
    d3, offset = parse(buffer, offset, 'int8')
    d4, offset = parse(buffer, offset, 'int8')
    d5, offset = parse(buffer, offset, 'uint32')
    d6 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int16')
        d6.append(val)
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4, 'D5': d5, 'D6': d6}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


pprint(main(b'IMZY:\x86<\x08\x8er5\x9d&I\xa4\x00|\xe0>2P\x1fv\x8e7+\xb6\xc7'
            b'\x93\xed\xb8\xc6\xe9\xc1\x0b\x0c]d\xe9e*\xca\xaf\xf2\x9b[\xf7yv\x05-\\'
            b'\x08\xc9Ac\xbd,\xbc$/\x02\xa2\xd1\xe4\xa0\x12\xe5n\x99l\x17\x1bn\xdcyz.-v'
            b'P\xdc\xf97\x1e\xd2\x0b\x90=\x15\xe1\xbe\x00\x11\x00*\x00C\xdc\xdc'
            b'c\xbc\x82\x1f\xbf)\xee\xb6\x00\x00\x00\x02\x00b\xc0\xba~\xd0\xd6)'
            b'\x00\x02\x00d2\xbd[\x99\x01\x00\x00\x00\x03\x00\x00\x00\\\x00h\xbf'
            b'\xdb\x17\xf5\xdc\xd6\xcaX'))
pprint(main(b'IMZY:\xbe\xf88\xe75\x1a\x00[o\xc8\x00h\xfe^\n\xde\xff\xfd:\xce\xe0U\x9c'
            b'\x12wJ!\xa2N\x03\xe4\x12\xfcTy\x1bv\x96\xd7\x89\x92*\xdeGS\xder\x8d\xfeL\x0b'
            b'[\x0c\xd3\x80\x16\x96\xf6\xc1I\xa1\x88\x00\x11\x00*mz\xe6H\x9c\xe2\xdc\x19C'
            b'jt\xe5\x01?P\xd4\x93\x00\x00\x00\x03\x00G\xa8\r\x12D\x9f\\\x00\x05\x00J'
            b'\xae\xbe\xa7\xe8\x1d\x00\x00\x00\x02\x00\x00\x00C\x00T\xbf\xeb\x0f,\x04'
            b'\t\xb5\xfa'))
