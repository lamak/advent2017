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
print('day 3, part 1: {}'.format(manhattan))
