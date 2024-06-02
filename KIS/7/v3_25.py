def main(x):
    x3 = {'KRL': 0, 'HCL': 1}
    x0 = {1990: 2, 1987: 3}
    x33 = {'KRL': 4, 'HCL': 5}
    x333 = {'KRL': 6, 'HCL': 7}
    x4 = {'TEXT': 8, 'SCALA': 9}

    x1 = {'ORG': x3[x[3]], 'P4': x0[x[0]]}
    x11 = {'ORG': x33[x[3]], 'P4': x333[x[3]]}
    x00 = {1990: x4[x[4]], 1987: 10}

    x44 = {'TEXT': x1[x[1]], 'SCALA': x11[x[1]]}
    x111 = {'ORG': x00[x[0]], 'P4': 11}

    ini = {'QMAKE': x44[x[4]], 'C++': x111[x[1]], 'MUPAD': 12}
    return ini[x[2]]


print(main([1987, 'ORG', 'C++', 'KRL', 'TEXT']))
print(main([1987, 'P4', 'C++', 'KRL', 'TEXT']))
print(main([1990, 'ORG', 'C++', 'KRL', 'TEXT']))
print(main([1990, 'ORG', 'QMAKE', 'KRL', 'SCALA']))
print(main([1987, 'ORG', 'MUPAD', 'KRL', 'SCALA']))
