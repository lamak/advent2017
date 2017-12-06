import operator

f = open('day6.data').read()
f = [int(x) for x in f.split(' ')]

i, value = max(enumerate(f), key=operator.itemgetter(1))
print(f)
print(i, value)
#
# while f[i] > 0:
#     for x in range(1, f[i]):
#         f[i + x] += 1
#         f[i] -= 1
