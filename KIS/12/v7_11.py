from struct import unpack_from, calcsize


class Types:
    double = "d"
    int32 = "i"
    int16 = "h"
    uint16 = "H"
    uint8 = "B"
    int8 = "b"
    int64 = "q"
    uint32 = "I"
    char = "c"
    uint64 = "Q"
    float = "f"


class BinaryReader:
    def __init__(self, data, offset, order="<"):
        self.data = data
        self.offset = offset
        self.order = order

    def jump_to(self, offset):
        reader = BinaryReader(self.data, offset, self.order)
        return reader

    def read(self, frmt):
        data = unpack_from(self.order + frmt, self.data, self.offset)
        self.offset += calcsize(frmt)
        return data[0]


def read_d(reader):
    d1 = reader.read(Types.uint32)
    d2 = reader.read(Types.float)
    d3 = [reader.read(Types.uint32) for _ in range(6)]
    d4 = reader.read(Types.double)
    d5 = reader.read(Types.int64)
    d6 = reader.read(Types.uint64)
    d7 = [reader.read(Types.uint16) for _ in range(2)]
    return dict(D1=d1, D2=d2, D3=d3, D4=d4, D5=d5, D6=d6, D7=d7)


def read_c(reader):
    c1 = reader.read(Types.float)
    c2_size = reader.read(Types.uint32)
    c2_offset = reader.read(Types.uint32)
    c2_reader = reader.jump_to(c2_offset)
    c2 = ""
    for _ in range(c2_size):
        c2 += c2_reader.read(Types.char).decode()
    c3_size = reader.read(Types.uint32)
    c3_offset = reader.read(Types.uint16)
    c3_reader = reader.jump_to(c3_offset)
    c3 = [c3_reader.read(Types.uint32) for _ in range(c3_size)]
    return dict(C1=c1, C2=c2, C3=c3)


def read_b(reader):
    b1 = reader.read(Types.int32)
    b2 = reader.read(Types.double)
    return dict(B1=b1, B2=b2)


def read_a(reader):
    a1 = reader.read(Types.int8)
    a2 = reader.read(Types.uint16)
    b_size = reader.read(Types.uint32)
    b_offset = reader.read(Types.uint16)
    b_reader = reader.jump_to(b_offset)
    a3 = [read_b(b_reader) for _ in range(b_size)]
    a4 = read_c(reader)
    a5 = reader.read(Types.uint64)
    a6 = reader.read(Types.int8)
    a7 = read_d(reader)

    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7)


def main(data):
    return read_a(BinaryReader(data, 4))


from pprint import pprint

pprint(main((b'\x87TOM\xd3\xeb7\x04\x00\x00\x00d\x00\x9d\x18??\x02\x00\x00\x00\x94\x00\x00'
             b'\x00\x03\x00\x00\x00\x96\x00\x1a\xa2\xd5W\xafc\x02TC\xcc\xa7\xe6\xdesF\xd2>'
             b'\x13)\x91vV\xff\x18\xca\xd1t\x93K\xe9]\x88\xb6\xacK\xf1\x0f\xb8\xe9\xed\x19'
             b'b~lw\xe0s\xee?\xc9F\x1c\xc9\xc3\\\xa3\x166J\x93\xd3\x1a\x1b\x14\x17'
             b"\xe7'<\xecXv\x82V\xa2]\x16y\xdfq\xee\xbf\x14\xe4\xb9\xa5\x0e\xd7\x978TJ\xeb?"
             b'n\xa9gA\xa8>\xef-\xeb|\xc8?\xe9\xf1\x9c\x8e\xb0\x17\x9c\xf82\xc4\xcf?avZ\x00'
             b'a\x8f\xa0\x1b\xa7\xc9\xdf\xcc5\x81')))
