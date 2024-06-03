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
    offset = 4
    a1, offset = parse_b(buffer, offset)
    a2, offset = parse(buffer, offset, 'float')
    a3, offset = parse(buffer, offset, 'int16')
    a4 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse_c(buffer, adr_offset)
        a4.append(val)
    a5_offset, offset = parse(buffer, offset, 'uint32')
    a5, _ = parse_e(buffer, a5_offset)
    return {'A1': a1, 'A2': a2, 'A3': a3,
            'A4': a4, 'A5': a5}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'int8')
    b2, offset = parse(buffer, offset, 'uint64')
    b3, offset = parse(buffer, offset, 'uint32')
    b4 = ''
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        b4 += (val.decode())
    return {'B1': b1, 'B2': b2,
            'B3': b3, 'B4': b4}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'uint64')
    c2_offset, offset = parse(buffer, offset, 'uint32')
    c2, _ = parse_d(buffer, c2_offset)
    c3, offset = parse(buffer, offset, 'uint8')
    c4, offset = parse(buffer, offset, 'int32')
    c5, offset = parse(buffer, offset, 'int64')
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4,
            'C5': c5}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'double')
    d2, offset = parse(buffer, offset, 'int16')
    d3, offset = parse(buffer, offset, 'int16')
    d4, offset = parse(buffer, offset, 'int8')
    d5, offset = parse(buffer, offset, 'uint16')
    b2 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        b2.append(val)
    return {'D1': d1, 'D2': d2, 'D3': d3}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


data = (b'AXFFYz\xa7\x80\xfeL\xdb\x00\x00\x00\x84+Ywk@"\x00\x02\x00\x95?\xe8n'
        b'\xbc}\xcfoLE\xeb!\xff?\xe5hs\xec(\x06\xf0\xafta\xd7<Oa\xed\xd8}\xc5'
        b'\x9a\xad\xe9\xafX\xa5H\x1d\xdav\x9cWs\xbf\xec\x895.\xd09\xb8\xbfs\xd1'
        b'R\x15\x0c\x00\x05\x000\xa7gW\xdbV\xd3X[\xf1\x03\x12\n\xdd\x8b\x8d\x88R'
        b'\xec\xb9\xed\xcb\xb6?\xc98/\n\x87\xce\xd0=ND\xceM\xaf\x00\x04\x00\\\x17'
        b'v%\x04\xf2\x00\x02\x00\x00\x00.\x17\xd3uZ\x8d\xc5I\x00D\x00l\xbe\xb8\xf2'
        b'\xa9')

from pprint import pprint

pprint(main(data))
