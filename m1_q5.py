list_a = []
for i in range(4):
    list_a.append(2 * i)
print(list_a)

list_b = [21, 22, 23, 24]
list_c = []
for i in range(4):
    list_c.append(list_b[i] // (3 * (i + 1)))
print(list_c)

list_d = [2, 4, 1, 6, 9, 3, 5, 7]
d = 2
while d < 12:
    list_d.pop(11 % d)
    d += 2
print(list_d)

list_e = [1, 2, 2, 7]
j = 0
for cd in [7, 3, 2, 6, 5]:
    if cd in list_e:
        list_e.remove(cd)
        list_e.insert(j, 2 * cd)
        j += 1
print(list_e)

result = ''
for e in [20, 6, -2, 12]:
    if (e + 4) ** 2 < 30:
        result += 'A'
    elif 4 < e / 3:
        result += 'B'
    else:
        result += 'C'
print(result)
