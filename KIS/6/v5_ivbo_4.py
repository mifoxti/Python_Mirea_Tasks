from math import ceil


def main(igrik):
    tigr = {9 * i + ceil(i / 6) for i in igrik if i > -99}
    zluka = igrik.union(tigr)
    bigl = tigr.union(zluka)
    return (len(zluka)
            + sum(cerbe * beta for cerbe in zluka
                  for beta in bigl))


print(main({-63, 2, -90, 12, -99, -48, -78, -76, 27, 29}))  # = 8964055
print(main({36, 70, -58, 72, -56, 42, 75, -76, -73, 95}))  # = 1674456
