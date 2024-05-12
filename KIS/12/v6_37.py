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
    offset = 3
    a1, offset = parse(buffer, offset, 'uint64')
    a2, offset = parse(buffer, offset, 'double')
    a3, offset = parse_b(buffer, offset)
    a4_offset, offset = parse(buffer, offset, 'uint32')
    a4, _ = parse_e(buffer, a4_offset)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4}, offset


def parse_b(buffer, offset):
    b1_offset, offset = parse(buffer, offset, 'uint32')
    b1, _ = parse_c(buffer, b1_offset)
    b2 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        b2.append(val)
    b3, offset = parse(buffer, offset, 'float')
    b4, offset = parse(buffer, offset, 'int64')
    b5 = []
    for _ in range(4):
        val, offset = parse(buffer, offset, 'int16')
        b5.append(val)
    b6, offset = parse(buffer, offset, 'int16')
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4,
            'B5': b5, 'B6': b6}, offset


def parse_c(buffer, offset):
    b3size, offset = parse(buffer, offset, 'uint32')
    b3offs, offset = parse(buffer, offset, 'uint32')
    c1 = []
    for _ in range(b3size):
        val, b3offs = parse_d(buffer, b3offs)
        c1.append(val)
    c2, offset = parse(buffer, offset, 'int64')
    c3, offset = parse(buffer, offset, 'int32')
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'int16')
    d2, offset = parse(buffer, offset, 'int32')
    d3 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint8')
        d3.append(val)
    d4, offset = parse(buffer, offset, 'float')
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'double')
    e2, offset = parse(buffer, offset, 'int64')
    e3, offset = parse(buffer, offset, 'int16')
    e4, offset = parse(buffer, offset, 'float')
    e5, offset = parse(buffer, offset, 'int32')
    e6 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint64')
        e6.append(val)
    return {'E1': e1, 'E2': e2, 'E3': e3, 'E4': e4,
            'E5': e5, 'E6': e6}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


pprint(main(b'VPT]r\x89\x86\x88\xd4]M\x00$[J|3\xab\xbfY\x00\x00\x00\x02\x00m\x00\x01'
            b'\x02H?\x02\xe7\xeb.\xf3\xa7\xb9\xe71\xd2z\x15\x1d-\x81s\x90F\x7f\x00\x00'
            b"\x00\xbf,'\t\xf9\xed\xacZ\xfd\x06\x02\x00\x00\x005\x00fA\xa0>\xce\x02\xb5"
            b'\x98e\xf7\x02\x00\x00\x007\x00\xcb\xd9}\xbe\x02\x00\x00\x009\x00\x00'
            b'\x00\x98\x1e\xd4-\x10Q"\xc2\xcaB\x10\xa3\xc6\xd9\xac\x93\x03\xf5*'
            b'}\x98\xa6\x91\xbfB\x91\xcb\x91\xc2\xee0\xa2E\xe0D\x14\xd6\xbf\x8f'
            b'\xbf\xe6\x8e\xa7\xefL\x97^\xdd\xfc\x805?`_,\x00\x02\x00\x00\x00o\x00'))
