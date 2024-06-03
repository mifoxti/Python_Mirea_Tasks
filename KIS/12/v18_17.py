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
    offset = 3
    a1 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'float')
        a1.append(val)
    a2, offset = parse_b(buffer, offset)
    a3 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint64')
        a3.append(val)
    a4 = []
    for _ in range(8):
        val, offset = parse(buffer, offset, 'float')
        a4.append(val)
    return {'A1': a1, 'A2': a2, 'A3': a3,
            'A4': a4}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'int16')
    b2_offset, offset = parse(buffer, offset, 'uint16')
    b2, _ = parse_c(buffer, b2_offset)
    b3, offset = parse(buffer, offset, 'uint16')
    b4, offset = parse(buffer, offset, 'uint16')
    b5, offset = parse(buffer, offset, 'int16')
    b6, offset = parse(buffer, offset, 'float')
    b7 = []
    array_size, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_size):
        a3_offset, adr_offset = parse(buffer, adr_offset, 'uint32')
        val, _ = parse_d(buffer, a3_offset)
        b7.append(val)
    b8, offset = parse(buffer, offset, 'uint16')
    return {'B1': b1, 'B2': b2,
            'B3': b3, 'B4': b4,
            'B5': b5, 'B6': b6,
            'B7': b7, 'B8': b8}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'int8')
    c2, offset = parse(buffer, offset, 'int16')
    c3, offset = parse(buffer, offset, 'int8')
    c4, offset = parse(buffer, offset, 'float')
    c5, offset = parse(buffer, offset, 'int8')
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4,
            'C5': c5}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'uint64')
    d2, offset = parse(buffer, offset, 'double')
    d3, offset = parse(buffer, offset, 'uint32')
    d4, offset = parse(buffer, offset, 'uint16')
    d5, offset = parse(buffer, offset, 'int8')
    return {'D1': d1, 'D2': d2, 'D3': d3,
            'D4': d4, 'D5': d5}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


data = (b'IMX\x04\x00\x00\x00C\x00e\xd0S\x00\xb8|\x8a\x99\xbb\xa3\xb9\xa9z\xbf\x02'
        b'\x00\x8a\x00_\x18\x02\x00\x92\x00\x00\x00\x8fq\x8e>\x91\xcf}?r\xf5M?\xb1'
        b'd\x18>y\xea\x07?\x13\x85\xf3<\xea*\x01\xbfc\x92}>\xcdO1\xbe8\xe7{\xbe\xd5'
        b'}\x9f\xbe}\x89q\xbf\x06\xdcJ\xce\x1c\xf4o\xbeS\xd4\x93\xe3\xfd'
        b'\xbc\x97\x91\xaa\xc0\xd5\x81\x92W9\x91\xbf\xf4\xefZ7\x82\xb8\xa7\x92'
        b'\x7f\xd3!Z\x85\xa4\xe00x\x97\xf4\xcdm\xdf?*\xd2Y\xc7\xff\xfcN\\\x00'
        b'\x00\x00s\x00\x00\x00\xf2\xfe\xbb\x89\xacA\xffcew\xa4\xb0\xef\xdaa\x19')

from pprint import pprint

pprint(main(data))
