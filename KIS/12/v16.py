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
    a1, offset = parse(buffer, offset, 'double')
    a2, offset = parse(buffer, offset, 'uint16')
    a3, offset = parse(buffer, offset, 'uint32')
    a4_offset, offset = parse(buffer, offset, 'uint16')
    a4, _ = parse_b(buffer, a4_offset)
    a5, offset = parse(buffer, offset, 'double')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4, 'A5': a5}, offset


def parse_b(buffer, offset):
    b1_offset, offset = parse(buffer, offset, 'uint32')
    b1, _ = parse_c(buffer, b1_offset)
    b2, offset = parse(buffer, offset, 'uint8')
    b3 = ''
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        b3 += (val.decode())
    b4, offset = parse_e(buffer, offset)
    b5 = []
    for _ in range(3):
        val, offset = parse(buffer, offset, 'float')
        b5.append(val)
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4,
            'B5': b5}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'float')
    c2 = []
    for _ in range(2):
        a, offset = parse_d(buffer, offset)
        c2.append(a)
    return {'C1': c1, 'C2': c2}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'int32')
    d2, offset = parse(buffer, offset, 'int8')
    d3, offset = parse(buffer, offset, 'int64')
    return {'D1': d1, 'D2': d2, 'D3': d3}, offset


def parse_e(buffer, offset):
    e1, offset = parse(buffer, offset, 'float')
    e2 = []
    for _ in range(8):
        val, offset = parse(buffer, offset, 'int32')
        e2.append(val)
    e3, offset = parse(buffer, offset, 'uint16')
    e4, offset = parse(buffer, offset, 'int64')
    return {'E1': e1, 'E2': e2, 'E3': e3, 'E4': e4}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


data = (b'jPNO\xb6x\xfe\x01\xa4\x88\xeb\xbfE`C\xee\xa7:<\x00P\xa4x]\x02\x0f\xe4?'
        b'\xb8)S\xbfb\xb3E\x112\x91qfR\x93D\x88l\xa4A\x03\xff\x13Z(\x8eq\xdd\xa6'
        b'\x97\xcftg\x1c\x00\x00\x00\x94\x02\x00:\x00@\xf6z\xbf\x86\x9f\xb8'
        b'\xa9\xfdZ\xdc\xc3\xd42/o\x1aH\xce\xa9\x12\x17\xf12\xe6\xb2\xf2l\xe3,\x99'
        b"l\xe6lP\xb8q\xd3\xdc\x1a7\xbc\xeb[\xb8'\xf2WB?aC\xce=Cjw\xbe")

from pprint import pprint

pprint(main(data))
