
def find_quart(samples):
    n = len(samples)

    return round((samples[n//2-1]+samples[n//2])/2) if n % 2 == 0 else samples[n//2]


def find_quarts(x):
    n = len(x)
    x.sort()
    Q2 = find_quart(x)
    if n % 2 != 0:
        x.remove(Q2)
    lower = x[:n // 2]
    upper = x[n // 2:]
    Q1 = find_quart(lower)
    Q3 = find_quart(upper)
    return [Q1, Q2, Q3]


# file = open('./input', 'r')
# n = int(file.readline().strip())
# x = list(map(int, file.readline().split()))
# f = list(map(int, file.readline().split()))
n = int(input().strip())
x = list(map(int, input().strip().split()))
f = list(map(int, input().strip().split()))
s = []
for idx, i in enumerate(f):
    for j in range(i):
        s.append(x[idx])
quarts = find_quarts(s)
print("{:.1f}".format(quarts[2]-quarts[0], 1))
