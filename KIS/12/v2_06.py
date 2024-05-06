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
    offset = 4
    a1, offset = parse_b(buffer, offset)
    a2_offset, offset = parse(buffer, offset, 'uint16')
    a2, _ = parse_d(buffer, a2_offset)
    a3 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint64')
        a3.append(val)
    return {'A1': a1, 'A2': a2, 'A3': a3}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'float')
    b2 = []
    for _ in range(7):
        b2_offset, offset = parse(buffer, offset, 'uint16')
        val, _ = parse_c(buffer, b2_offset)
        b2.append(val)
    return {'B1': b1, 'B2': b2}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'int8')
    c2 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint8')
        c2.append(val)
    c3, offset = parse(buffer, offset, 'uint32')
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset


def parse_d(buffer, offset):
    d1 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint8')
        d1.append(val)
    d2, offset = parse(buffer, offset, 'uint8')
    return {'D1': d1, 'D2': d2}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


pprint(main(b'\xb1JZX\xbe9\\\x0e\x00 \x00+\x008\x00C\x00N\x00[\x00g\x00t\x00\x02\x00\x00'
 b'\x00{P\xd1u\x00\x02\x00\x1e\x0bE~\x1d\xe1w\xc2\x00\x02\x00)\x82\xc2\xf3\x16'
 b'\x9dr\xd0\xb9\xd8\x00\x04\x004\x8a\xe8~\x9a\xb9<\xfa\x00\x02\x00A'
 b'\x92\x88j\xe2\xcb\xd1\x19\x00\x02\x00LC\xe5\xf9\x89\xee\xe2\x07\xcdI'
 b'\x00\x04\x00W[h\xda\x0c?\xf0\x95\xb8\x00\x03\x00d\xd7\xeb+bN\xb5\xca\xa9'
 b'\x00\x04\x00\x00\x00p|*\x91B\x86\xcf"\xc7\xd3\x06\\\xa8t\xe2\xb2\x16\x16'))
