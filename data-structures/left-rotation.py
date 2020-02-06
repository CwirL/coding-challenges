n = 5
d = 4
a = [1, 2, 3, 4, 5]


for i in range(d):
    a.append(a.pop(0))
for el in a:
    print(el, end=" ")