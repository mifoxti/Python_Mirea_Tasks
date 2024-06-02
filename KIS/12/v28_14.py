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
    offset = 5
    a1 = []
    for _ in range(2):
        a1_offset, offset = parse(buffer, offset, 'uint32')
        val, _ = parse_b(buffer, a1_offset)
        a1.append(val)
    a2, offset = parse(buffer, offset, 'uint64')
    return {'A1': a1, 'A2': a2}, offset


def parse_b(buffer, offset):
    b1, offset = parse_c(buffer, offset)
    b2 = []
    for _ in range(5):
        val, offset = parse(buffer, offset, 'int8')
        b2.append(val)
    return {'B1': b1, 'B2': b2}, offset


def parse_c(buffer, offset):
    c1_offset, offset = parse(buffer, offset, 'uint32')
    c1, _ = parse_d(buffer, c1_offset)
    c2, offset = parse(buffer, offset, 'double')
    c3 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint8')
        c3.append(val)
    c4 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int32')
        c4.append(val)
    c5, offset = parse(buffer, offset, 'uint64')
    c6, offset = parse(buffer, offset, 'int8')
    c7, offset = parse(buffer, offset, 'int8')
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4,
            'C5': c5, 'C6': c6, 'C7': c7}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'int16')
    d2, offset = parse(buffer, offset, 'uint32')
    d3, offset = parse(buffer, offset, 'float')
    d4, offset = parse(buffer, offset, 'uint32')
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'!SSNM\x00\x00\x008\x00\x00\x00\x83\x1d\x1b\x16\xe9\x18\xc8\x85\x00tj\xfb'
            b"\x98J\xb4\xbfw\xac\x98\x90\xaf\xd0\xd3\x8b'\xb1\x07\xe9\x9c\x06&s:\x8a$\xb8"
            b'W\xb5R\xc1\xfbH\xc1\x1b\x00\x00\x00\x15?\xed\x9a\xc94b\x8b\xe0'
            b'\x00\x05\x00\x00\x00#\x00\x04\x00\x00\x00(\xf6q\x95\xaf\xe9h\xbc\xea8_s\xe1'
            b'"c-\x85\x9c\\\x18\xa3\x12>\xba\xf1\xa3p\xdb1 /\xd9\xc0\x89B-x\xac\xd6\xd0%'
            b'\xb9\x91\xa7\x8f\x04\xe4\xe9A\xd4w\xb1\x00\x00\x00_\xbf\xda\xfb!:'
            b'\xb6\xed\x1c\x00\x06\x00\x00\x00m\x00\x04\x00\x00\x00s\xd7\x91$\xba\xef'
            b'y\xa1>\x1a\x07\xe4\xf9|S,'))
