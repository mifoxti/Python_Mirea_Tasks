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
    offset = 4
    a1, offset = parse(buffer, offset, 'int16')
    a2 = ''
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        a2 += (val.decode())
    a3, offset = parse(buffer, offset, 'uint16')
    a4, offset = parse(buffer, offset, 'uint64')
    a5 = []
    for _ in range(2):
        a5_offset, offset = parse(buffer, offset, 'uint16')
        val, _ = parse_b(buffer, a5_offset)
        a5.append(val)
    a6, offset = parse_c(buffer, offset)
    a7_offset, offset = parse(buffer, offset, "uint32")
    a7, offset = parse_d(buffer, a7_offset)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5, 'A6': a6, 'A7': a7}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'uint8')
    b2, offset = parse(buffer, offset, 'int16')
    b3 = []
    for _ in range(6):
        val, offset = parse(buffer, offset, 'uint8')
        b3.append(val)
    b4, offset = parse(buffer, offset, 'int32')
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'int64')
    c2, offset = parse(buffer, offset, 'int64')
    c3, offset = parse(buffer, offset, 'uint32')
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'uint16')
    d2 = []
    for _ in range(4):
        val, offset = parse(buffer, offset, 'float')
        d2.append(val)
    return {'D1': d1, 'D2': d2}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


pprint(main(b'\xedHTJ\xe6i\x05\x00\x00\x002\x00<-\xe9\xaa\x973\x8e\r\xaeG7\x00'
            b"D\x00\xc7\xb9.\x19\x16M\xe3\xf8\x82\x8ak\xae\x8b4'\x08\x87\xb1qqQ\x00"
            b'\x00\x00tegmk\xb2MM\xb1\xc7\x99k \x92\xd1\xf5\x159\x984\xad\x1e'
            b'\xa9\xab\x92\x9d\xeb\xce|=\x89Us\x8fS\x8e>~j6\xbf+\xfc\xc4\xbdjK->'))
