def script(check, x, y):
    level = check("level")
    gold = check("gold", x, y)

    if level == 1:
        if gold != 0:
            return "take"
        if not check("wall", x + 2, y):
            return "right"
        return "down"

    elif level == 2:
        if gold != 0:
            return "take"
        if not check("wall", x + 2, y) and check("wall", x, y + 1):
            return "right"
        if check("gold", x, y + 1) != 0:
            return "down"
        if not check("wall", x, y - 1):
            return "up"
        return "right"

    elif level == 3:
        if gold != 0:
            return "take"

        def is_wall(a, b):
            return check("wall", x + a, y + b)

        if is_wall(-1, 0) and not is_wall(0, -1):
            return "up"
        if is_wall(0, -1) and not is_wall(1, 0):
            return "right"
        if is_wall(-1, -1) and not is_wall(0, -1):
            return "up"
        if is_wall(1, 0) and not is_wall(0, 1):
            return "down"
        if is_wall(1, -1) and not is_wall(1, 0):
            return "right"
        if is_wall(-1, 1) and not is_wall(-1, 0):
            return "left"
        if is_wall(0, 1) and not is_wall(-1, 0):
            return "left"
        if is_wall(1, 1) and not is_wall(0, 1):
            return "down"

    elif level == 4:
        if gold != 0:
            return "take"

        positions = [(3, 16), (4, 16), (10, 13), (10, 12)]
        for pos in positions:
            if (x, y) == pos:
                return "right" if pos[1] == 16 else "up"

        def is_wall(a, b):
            return check("wall", x + a, y + b)

        if is_wall(-1, 0) and not is_wall(0, -1):
            return "up"
        if is_wall(0, -1) and not is_wall(1, 0):
            return "right"
        if is_wall(-1, -1) and not is_wall(0, -1):
            return "up"
        if is_wall(1, 0) and not is_wall(0, 1):
            return "down"
        if is_wall(1, -1) and not is_wall(1, 0):
            return "right"
        if is_wall(-1, 1) and not is_wall(-1, 0):
            return "left"
        if is_wall(0, 1) and not is_wall(-1, 0):
            return "left"
        if is_wall(1, 1) and not is_wall(0, 1):
            return "down"

    elif check("level") == 5:
        if (check("gold", x, y) != 0):
            return "take"
        if (check("gold",x+1,y)!=0):
            return "right"
        if (check("gold",x-1,y)!=0):
            return "left"
        if (check("gold",x,y+1)!=0):
            return "down"
        if (check("gold",x,y-1)!=0):
            return "up"
        # print(x, y)
        # if check("gold", x, y) != 0:
        #     return "take"
        #
        # left_wall = check("wall", x - 1, y)
        # right_wall = check("wall", x + 1, y)
        # up_wall = check("wall", x, y - 1)
        # down_wall = check("wall", x, y + 1)
        # if not left_wall:
        #     "left"
        #
        #
        # # if x == 8 and y == 7:
        # #     return "left"
        # # if x == 7 and y == 7:
        # #     return "up"
        # # if x == 7 and y == 6:
        # #     return "up"
        # # if x == 7 and y == 5:
        # #     return "left"
        # # if x == 6 and y == 5:
        # #     return "up"


