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
    a1, offset = parse(buffer, offset, 'float')
    a2, offset = parse(buffer, offset, 'int8')
    a3, offset = parse_b(buffer, offset)
    a4 = []
    for _ in range(2):
        d_offset, offset = parse(buffer, offset, 'uint16')
        d, _ = parse_d(buffer, d_offset)
        a4.append(d)
    a5, offset = parse(buffer, offset, 'int16')
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4, 'A5': a5}, offset


def parse_b(buffer, offset):
    b1, offset = parse(buffer, offset, 'uint64')
    b2, offset = parse(buffer, offset, 'double')
    b3, offset = parse_c(buffer, offset)
    b4, offset = parse(buffer, offset, 'int32')
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4}, offset


def parse_c(buffer, offset):
    c1, offset = parse(buffer, offset, 'double')
    c2 = ''
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'char')
        c2 += (val.decode())
    c3 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'int32')
        c3.append(val)
    return {'C1': c1, 'C2': c2, 'C3': c3}, offset


def parse_d(buffer, offset):
    d1 = []
    array_siz, offset = parse(buffer, offset, 'uint16')
    adr_offset, offset = parse(buffer, offset, 'uint16')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint16')
        d1.append(val)
    d2, offset = parse(buffer, offset, 'uint64')
    d3, offset = parse(buffer, offset, 'uint64')
    d4 = []
    array_siz, offset = parse(buffer, offset, 'uint32')
    adr_offset, offset = parse(buffer, offset, 'uint32')
    for _ in range(array_siz):
        val, adr_offset = parse(buffer, adr_offset, 'uint16')
        d4.append(val)
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4}, offset


def main(data):
    result, _ = parse_a(data, 0)
    return result


from pprint import pprint

pprint(main(b'DDP\x81?v\x076\xdcg\xea-\xffv\x83v~\xbf\xb9\x98{<\xa0n\xd0?\xaf\xa8'
            b'4N\x81\xd8\xc0\x00\x00\x00\x04\x00\x00\x007\x00\x02\x00;\x8d\xea\xcd'
            b'\x8b\x00W\x00\x8fe\xb6zrdu\x90W\xde\xf2N\xcd\xf2Jf\xd8\x089\xe5\x83R\xfe{'
            b"T\x1c}\x99VY\xbe5\x11\xddu\x00\x02\x00C'N!\xe5\x9a\xd0\xb5\x16\xbc%\x8d\xab3"
            b'\x85]\t\x00\x00\x00\x08\x00\x00\x00G@\xa6\xec\x0e\xfc\xa7\rW\xcfM\xb9Y\xb9'
            b'\t{B\x9ce^\xce}\xde\x83\xfcq\xf0\x83N\x00\x07\x00s\x98\xa6\xaaX\xb2'
            b'\xfcn\n\xaf$\xd0\x03\r\xad\xfe*\x00\x00\x00\x07\x00\x00\x00\x81'))
