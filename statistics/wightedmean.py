file = open('./input', 'r')
n = int(file.readline().strip())
x = list(map(int, file.readline().split()))
w = list(map(int, file.readline().split()))
mean = round(sum([i*j for i, j in zip(x, w)])/sum(w), 1)
print(mean)