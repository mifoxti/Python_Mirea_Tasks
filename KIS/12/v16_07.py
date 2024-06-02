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
    a1, offset = parse(buffer, offset, 'float')
    a2, offset = parse(buffer, offset, 'int64')
    a3 = []
    array_size, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_size):
        val, adr_offset = parse_b(buffer, adr_offset)
        a3.append(val)
    return {'A1': a1, 'A2': a2, 'A3': a3}, offset


def parse_b(buffer, offset):
    b1, offset = parse_c(buffer, offset)
    b2, offset = parse(buffer, offset, 'float')
    b3, offset = parse(buffer, offset, 'uint8')
    return {'B1': b1, 'B2': b2, 'B3': b3}, offset


def parse_c(buffer, offset):
    c1 = []
    for _ in range(3):
        val, offset = parse(buffer, offset, 'int64')
        c1.append(val)
    c2, offset = parse(buffer, offset, 'int8')
    c3, offset = parse_d(buffer, offset)
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset


def parse_d(buffer, offset):
    d1, offset = parse(buffer, offset, 'float')
    d2 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint16')
        d2.append(val)
    d3, offset = parse(buffer, offset, 'uint32')
    d4, offset = parse(buffer, offset, 'int8')
    d5, offset = parse(buffer, offset, 'uint8')
    d6 = []
    for _ in range(7):
        val, offset = parse(buffer, offset, 'int8')
        d6.append(val)
    d7, offset = parse(buffer, offset, 'int32')
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4,
            'D5': d5, 'D6': d6, 'D7': d7}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'OQM\x97\x8e\x00\xbf8h\xd8A\x10\xd8\xd1\x04\x02\x00\x00\x00-\x00\x05\x99\xcc'
            b'\x89\xd4\x91\xb7\x88\xeb\xbd\x1a+7\x86)/\xf4l\xaa|\xb7\xc3,\xbb\xfcZW'
            b'\x15\x9f\xd7!C3(o\xb3}\x1b\xdf]\xa2f\x9e\x0cd\xe2e\xda\xae3@C\xbe\x06\x00'
            b'\x00\x00\x15\x00\x00\x00\xdb\x9d\xca\x15\xde\xf3\x19\x18\xb7\x802\xe4;\xf4'
            b'\xb2\xa9\xd6\x8c\xa4X>S\x87\x16_\xcb\xa4B\xe7\xd5\xad8^\x1fL\x8f\x7f\x93'
            b'\x0b\x87&ujP\x9e\xcf\x85\xc3a\x11\xbf\x06\x00\x00\x00!\x00\x00\x00t\xb4\xc5'
            b'\x9d\xa5a\xe4\xd0:\x8b\xafm\xff\xd2\xecs\xe7Na~?&'))
