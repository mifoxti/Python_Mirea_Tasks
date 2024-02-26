def decrypt(v, k):
    v0 = v[0]
    v1 = v[1]
    sum = 0xC6EF3720
    delta = 0x9E3779B9
    k0 = k[0]
    k1 = k[1]
    k2 = k[2]
    k3 = k[3]

    for i in range(32):
        v0 -= ((v1 << 4) + k0) ^ (v1 + sum) ^ ((v1 >> 5) + k1)
        v1 -= ((v0 << 4) + k2) ^ (v0 + sum) ^ ((v0 >> 5) + k3)
        sum -= delta

    return [v0, v1]


encrypted_data = [
    0xE3238557, 0x6204A1F8, 0xE6537611, 0x174E5747,
    0x5D954DA8, 0x8C2DFE97, 0x2911CB4C, 0x2CB7C66B,
    0xE7F185A0, 0xC7E3FA40, 0x42419867, 0x374044DF,
    0x2519F07D, 0x5A0C24D4, 0xF4A960C5, 0x31159418,
    0xF2768EC7, 0xAEAF14CF, 0x071B2C95, 0xC9F22699,
    0xFFB06F41, 0x2AC90051, 0xA53F035D, 0x830601A7,
    0xEB475702, 0x183BAA6F, 0x12626744, 0x9B75A72F,
    0x8DBFBFEC, 0x73C1A46E, 0xFFB06F41, 0x2AC90051,
    0x97C5E4E9, 0xB1C26A21, 0xDD4A3463, 0x6B71162F,
    0x8C075668, 0x7975D565, 0x6D95A700, 0x7272E637
]
decrypted_data = []
for i in range(0, len(encrypted_data), 2):
    decrypted_data.extend(decrypt([encrypted_data[i], encrypted_data[i + 1]], [0, 4, 5, 1]))

for data in decrypted_data:
    print(int(data))
