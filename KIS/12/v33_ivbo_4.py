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
    a1, offset = parse_b(buffer, offset)
    a2, offset = parse(buffer, offset, 'int16')
    a3 = []
    for _ in range(3):
        val, offset = parse(buffer, offset, 'uint8')
        a3.append(val)
    a4_offset, offset = parse(buffer, offset, 'uint16')
    a4, _ = parse_d(buffer, a4_offset)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'double')
    b2 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse_c(buffer, adr_offset)
        b2.append(val)
    b3 = []
    for _ in range(7):
        val, offset = parse(buffer, offset, 'int32')
        b3.append(val)
    return {'B1': b1, 'B2': b2, 'B3': b3}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'uint8')
    c2, offset = parse(buffer, offset, 'uint16')
    c3 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        c3.append(val)
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'int64')
    d2, offset = parse(buffer, offset, 'uint64')
    d3, offset = parse(buffer, offset, 'int16')
    d4, offset = parse(buffer, offset, 'uint8')
    d5, offset = parse(buffer, offset, 'int32')
    d6, offset = parse(buffer, offset, 'int32')
    return {'D1': d1, 'D2': d2, 'D3': d3,
            'D4': d4, 'D5': d5, 'D6': d6}, offset


def main(data):
    result, _ = parse_a(data, 5)
    return result


data = (b'\x16QWQL\x82gU\x91\x15\x05\xea?\x05\x00\x00\x00J\x00\x00\x00\xb7*\xc2'
        b'\xb8m\r\xdfSR\xeb\x9e\xf3\x14\xc3\xec\x80\x87\x9e\xaakl\xb2\x9e{\xf4\xa2\x06'
        b'@\xe0\x90fl\x7fm\x00?\xc3\x84\x94\x90\xe4\xca\xd0P\x81\xb3\x88\xc7\xad\\\xf6'
        b'+\x13\xea\x02\x1c\x06\x008\x00\x8fb\xb3\x04\x00>\x00\xf93\x87\x04'
        b'\x00B\x00\x06\x8a\x95\x02\x00F\x00\xc9\xd2P\x02\x00H\x00\xab\xd2^'
        b'\xf0\xda\x17\x1a\xd1\xd1\xc8L\xf8\x8b\xee\xc2\x0b+\xf0<\x8c5?hN+\xa8\x07')
from pprint import pprint

pprint(main(data))
