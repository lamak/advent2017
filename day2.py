checksum = 0
with open('day2.data') as f:
    raw = f.readlines()
clean = [x.replace('\n', '') for x in raw]
separated = [y.split('\t') for y in clean]
for row in separated:
    row = list(map(int, row))
    checksum += max(row) - min(row)

print('day2, part1: {}'.format(checksum))

checksum = 0
for row in separated:
    row = list(map(int, row))
    for element in row:
        for elementdiv in row:
            if element / elementdiv == element // elementdiv != 1:
                checksum += int(element / elementdiv)

print('day2, part2: {}'.format(checksum))
