from math import sqrt

n = int(input().strip())
x = list(map(int, input().strip().split()))
u = sum(x)/n
v = sum([(xi-u)**2 for xi in x])/n
s = sqrt(v)
print(round(s, 1))
