def script(check, x, y):
    if check("gold", x, y) != 0:
        return "take"
    elif check("gold", x + 1, y) != 0:
        return "right"
    elif check("gold", x - 1, y) != 0:
        return "left"
    elif check("gold", x, y + 1) != 0:
        return "down"
    elif check("gold", x, y - 1) != 0:
        return "up"
    else:
        all_w = []
        if not check("wall", x, y - 1):
            all_w.append('up')
        if not check("wall", x, y + 1):
            all_w.append('down')
        if not check("wall", x - 1, y):
            all_w.append('left')
        if not check("wall", x + 1, y):
            all_w.append('right')
        start_pos_1 = (x, y)

        end_pos = (0, 0)

        width, height = 35, 35
        v = [(x, y)]
        # словарь расстояний
        d = {(x, y): 0}
        while len(v) > 0:
            x, y = v.pop(0)
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if dx * dy != 0:
                        continue
                    if x + dx < 0 or x + dx >= width or y + dy < 0 or y + dy >= height:
                        continue
                    if not check("wall", x + dx, y + dy):
                        dn = d.get((x + dx, y + dy), -1)
                        if dn == -1:
                            d[(x + dx, y + dy)] = d[(x, y)] + 1
                            v.append((x + dx, y + dy))
        x1, y1 = start_pos_1

        def geet_path(v):
            path = [v]
            while v != (x1, y1):
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if dx * dy != 0 or (dx == 0 and dy == 0):
                            continue
                        x = v[0]
                        y = v[1]
                        if x + dx < 0 or x + dx >= width or y + dy < 0 or y + dy >= height:
                            continue
                        if d.get((x + dx, y + dy), -100) == d[v] - 1:
                            v = (x + dx, y + dy)
                            path.append(v)
            return path

        wdfsdf = 10000
        for z in range(30):
            for i in range(-z, z + 1):
                for j in range(-z, z + 1):
                    if check("gold", x + i, y + j):
                        dfdf = len(geet_path((x + i, y + j)))
                        if dfdf < wdfsdf:
                            end_pos = (x + i, y + j)
                            wdfsdf = dfdf

        path = geet_path(end_pos)
        y1, x1 = start_pos_1
        y2, x2 = path[-2]

        if y1 < y2:
            s = 'right'
        elif y1 > y2:
            s = 'left'
        elif x1 < x2:
            s = 'down'
        else:
            s = 'up'
        return s
