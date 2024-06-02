from struct import *


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
    a1 = ''
    for _ in range(7):
        val, offset = parse(buffer, offset, 'char')
        a1 += (val.decode())
    a2, offset = parse_b(buffer, offset)
    a3 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int32')
        a3.append(val)
    a4, offset = parse(buffer, offset, 'int16')
    a5, offset = parse_d(buffer, offset)
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4,
            'A5': a5}, offset


def parse_b(buffer, offset):
    b1 = []
    for _ in range(2):
        b, offset = parse_c(buffer, offset)
        b1.append(b)
    b2 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int8')
        b2.append(val)
    return {'B1': b1, 'B2': b2}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'double')
    c2, offset = parse(buffer, offset, 'float')
    return {'C1': c1, 'C2': c2}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'uint32')
    d2, offset = parse(buffer, offset, 'int64')
    d3, offset = parse(buffer, offset, 'uint64')
    return {'D1': d1, 'D2': d2, 'D3': d3}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'\xe4KAHphewapc?\xde\x8b>\x02-\xb6\xc0\xbf\x19\xa6\xda?\xd4~Y\xb0= \x80\xbe'
            b'^\x86\x90\x00\x00\x00\x02\x00C\x00\x02\x00E ShS\x87\xa8\xd8\xd7\xc1\x1dx'
            b'u\xf2\x01\xea\x9fl\xc9\xa1.\xb2\x86\xd8^\xe0H|\xdf\xb0<\xf0\x1f'))
