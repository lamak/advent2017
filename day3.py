with open('day3.data') as f:
    raw = f.read()
length = int(raw)


def move_right(x, y):
    return x + 1, y


def move_down(x, y):
    return x, y - 1


def move_left(x, y):
    return x - 1, y


def move_up(x, y):
    return x, y + 1


moves = [move_right, move_up, move_left, move_down]

moves_s = [move_down, move_left, move_up, move_up, move_right, move_right, move_down, move_down]

def gen_points(end):
    from itertools import cycle
    side = cycle(moves)
    n = 1
    pos = 0, 0
    times_to_move = 1
    while True:
        for z in range(2):
            move = next(side)
            for z in range(times_to_move):
                if n >= end:
                    return pos
                pos = move(*pos)
                n += 1

        times_to_move += 1


manhattan = sum(map(abs, gen_points(length)))


# print('day 3, part 1: {}'.format(manhattan))

def gen_points2(end):
    from itertools import cycle
    side = cycle(moves)
    path = []
    n = 1
    total = 1
    pos = 0, 0
    times_to_move = 1
    path.append((n, pos, total))
    while True:
        for z in range(2):
            move = next(side)
            for z in range(times_to_move):
                if n >= end:
                    return path
                pos = move(*pos)
                total += path[n - 1][2] + path[n-2][2]
                pos_s = pos

                n += 1
                path.append((n, pos, total))

        times_to_move += 1


for i in list(gen_points2(25)):
    print(i)
