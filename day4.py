with open('day4.data') as f:
    raw = f.readlines()
clean = [x.replace('\n', '') for x in raw]
print(len(raw))
counter = 0

for i in clean:
    lst = list(i.split(' '))
    if len(lst) != len(set(lst)):
        counter += 1
print('Day 4, part 1: {}'.format(len(clean) - counter))

charset = []
counter = 0
for string in clean:
    lst = list(string.split(' '))
    charset.append(list(''.join(sorted(word)) for word in lst))

for i, element in enumerate(charset):
    if len(element) == len(set(element)):
        counter += 1

print('Day 4, part 2: {}'.format(counter))
