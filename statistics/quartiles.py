def find_quart(samples):
    n = len(samples)
    return round((samples[n//2-1]+samples[n//2])/2) if n % 2 == 0 else samples[n//2]


n = int(input().strip())
x = list(map(int, input().strip().split()))
x.sort()
Q2 = find_quart(x)
if n % 2 != 0:
    x.remove(Q2)
lower = x[:n//2]
upper = x[n//2:]
Q1 = find_quart(lower)
Q3 = find_quart(upper)
print(Q1)
print(Q2)
print(Q3)
