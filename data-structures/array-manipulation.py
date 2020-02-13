def arrayManipulation(n, queries):
    arr = [0]*n
    for i in queries:
        arr[i[0] - 1] += i[2]
        if i[1] != len(arr):
            arr[i[1]] -= i[2]
        print(arr)
    maxval = 0
    itt = 0

    for q in arr:
        itt += q
        if itt > maxval:
            maxval = itt
    return maxval

file = open('./data', 'r')
mn = file.readline().rstrip().split()
n = int(mn[0])
m = int(mn[1])
queries = []
for _ in range(m):
    queries.append(list(map(int, file.readline().rstrip().split())))

result = arrayManipulation(n, queries)
print(result)