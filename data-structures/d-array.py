def dynamicArray(n, queries):
    seq_list = [[] for _ in range(n)]
    last_answer = 0
    sol = []
    for query in queries:
        [qtypqe, x, y] = query
        if qtypqe == 1:
            seq = seq_list[(x ^ last_answer) % n]
            seq.append(y)
        if qtypqe == 2:
            seq = seq_list[(x ^ last_answer) % n]
            last_answer = seq[y % len(seq)]
            sol.append(last_answer)
    for answer in sol:
        print(answer)


file = open('./data', 'r')
firstLine = file.readline().split()
n = int(firstLine[0])
q = int(firstLine[1])

queries = []
for i in range(q):
    queries.append(list(map(int, file.readline().split())))

dynamicArray(n, queries)
