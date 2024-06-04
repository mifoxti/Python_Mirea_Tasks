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
    a1, offset = parse(buffer, offset, 'uint32')
    a2_offset, offset = parse(buffer, offset, 'uint32')
    a2, _ = parse_b(buffer, a2_offset)
    a3 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint16')
        a3.append(val)
    return {'A1': a1, 'A2': a2, 'A3': a3}, offset


def parse_b(buffer, offset):
    b1, offset = parse_c(buffer, offset)
    b2_offset, offset = parse(buffer, offset, 'uint16')
    b2, _ = parse_e(buffer, b2_offset)
    b3 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int32')
        b3.append(val)
    return {'B1': b1, 'B2': b2,
            'B3': b3}, offset


def parse_c(buffer, offset):
    c1 = []
    for _ in range(4):
        a, offset = parse_d(buffer, offset)
        c1.append(a)
    c2, offset = parse(buffer, offset, 'int64')
    return {'C1': c1, 'C2': c2}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'int8')
    d2 = []
    for _ in range(5):
        val, offset = parse(buffer, offset, 'uint16')
        d2.append(val)
    return {'D1': d1, 'D2': d2}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'int32')
    e2, offset = parse(buffer, offset, 'double')
    e3, offset = parse(buffer, offset, 'double')
    e4, offset = parse(buffer, offset, 'double')
    return {'E1': e1, 'E2': e2, 'E3': e3,
            'E4': e4}, offset


def main(data):
    result, _ = parse_a(data, 3)
    return result


data = (b'RAO\xf5-\xb3OK\x00\x00\x00\x08\x00\x00\x00\x87\x00\x00\x00\xb2a\xdfM\xa0'
        b'\xd91\xfc\xb6\xc6\xe8\xbf\xe0\x03\x96I\xac\xce\xb6?\xd2\x03\xadd\x9b'
        b'\x10\xea\xbf\x1a!\xbe\xb7\x95\x88\x01\xb2\r\xafY\xc0x\x1eK\xd4%p<m\xf3'
        b'\xae\xac\xd1:\x82\xd1\xe8\x80\xcf\x98q\xbd\xdcY=\xdbU \xd6/Af\xc9\xce'
        b'\xa5\xad\xf6\x80*\x17\x95\xef\xe9\xb0\xf21\xd7Y$\x8c\x92\xb4\x93\x9a'
        b'\xd5\xfa\x99\xda\x16\x9d4\xc2N\xa8j\xa8\xf2P\x10\x13\x00\x07\x00\x00'
        b'\x00/\x00R\xd0K\xb3\xe4\xd7\xa6\x9aa\x0c\x14\xe4\xfdck`')

from pprint import pprint

pprint(main(data))
