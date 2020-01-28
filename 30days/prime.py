from math import sqrt, ceil
T = int(input())
solution = [None for z in range(T)]
for i in range(T):
    n = int(input())
    if n == 1:
        solution[i] = "Not prime"
        continue
    print(ceil(sqrt(n)))
    for j in range(2, ceil(sqrt(n))+1):
        print(j)
        if n % j == 0 and j != n:
            solution[i] = "Not prime"
            break
    if solution[i] is None:
        solution[i] = "Prime"

for z in solution:
    print(z)
