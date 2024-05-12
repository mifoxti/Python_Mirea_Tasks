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
    offset = 5
    a1 = []
    for _ in range(2):
        e, offset = parse_b(buffer, offset)
        a1.append(e)
    a2, offset = parse(buffer, offset, 'uint32')
    a3, offset = parse(buffer, offset, 'float')
    a4_offset, offset = parse(buffer, offset, 'uint16')
    a4, _ = parse_c(buffer, a4_offset)
    a5, offset = parse(buffer, offset, 'uint16')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'uint64')
    b2, offset = parse(buffer, offset, 'uint8')
    b3 = ''
    for _ in range(2):
        val, offset = parse(buffer, offset, 'char')
        b3 += (val.decode())
    return {'B1': b1, 'B2': b2, 'B3': b3}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'double')
    c2, offset = parse(buffer, offset, 'int32')
    c3, offset = parse_d(buffer, offset)
    c4, offset = parse(buffer, offset, 'uint8')
    c5, offset = parse(buffer, offset, 'uint32')
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4, 'C5': c5}, offset


def parse_d(buffer, offset):
    d1 = []
    for _ in range(5):
        val, offset = parse(buffer, offset, 'int16')
        d1.append(val)
    d2 = []
    for _ in range(6):
        val, offset = parse(buffer, offset, 'uint8')
        d2.append(val)
    d3, offset = parse(buffer, offset, 'int32')
    return {'D1': d1, 'D2': d2, 'D3': d3}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


pprint(main(b'WHZT$\xd0\xf6q\xc7@\xf8\xa0-\xb1he\xf7\xd4\xa5*\x1d\x99\xaa\xa6\x15te\xea'
 b"\x16\xb4\x8b\xae\xf6j\xbf'\x00\x1c5\x10\xdbC\xed\xacl\xe4?\x7f\x990\x07\xdf"
 b'\xa7\x8b\xef\xa92\xfc\xb7l\x86\xe3\x12\xdd\x00}9:\x8f&\x9a\xb6\xf88\xf57'))
