f = open('day5.data').readlines()
a = [int(row.strip()) for row in f]

step = 0
i = 0

while i < len(a):
    tmp = a [i]
    a[i] = a[i] + 1
    i = i + tmp
    step = step + 1
print(step, i)

