f = open('day5.data').readlines()
a = [int(row.strip()) for row in f]
b = [int(row.strip()) for row in f]

step = 0
i = 0

while i < len(a):
    tmp = a[i]
    a[i] += 1
    i += tmp
    step += 1
print('Day 5, part 1: {}'.format(step))

step = 0
i = 0

while i < len(b):
    tmp = b[i]
    if b[i] < 3:
        b[i] += 1
    else:
        b[i] -= 1
    i += tmp
    step += 1
print('Day 5, part 2: {}'.format(step))
