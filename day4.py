with open('day4.data') as f:
    raw = f.readlines()
clean = [x.replace('\n', '') for x in raw]
counter = 0
for i in clean:
    lst = list(i.split(' '))
    if len(lst) != len(set(lst)):
        counter +=1
print('Day 4, part 1: {}'.format(len(clean) - counter))