import sys

n = int(input().strip())
a = list(map(int, input().strip().split()))
numberOfSwaps = 0
for i in range(n):
    swaps = 0
    for j in range(n-1):
        if a[j] > a[j + 1]:
            a[j], a[j+1] = a[j+1], a[j]
            swaps += 1
    numberOfSwaps += swaps
    if swaps == 0:
        break

print("Array is sorted in " + str(numberOfSwaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[-1]))
