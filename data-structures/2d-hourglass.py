def hourglassSum(arr):
    sums = []
    message = "first row = {f}, second row = {s}, third row = {t}, hourglass = {h}"
    for i in range(4):
        for j in range(4):
            fsum = sum(arr[j][i:i+3])
            ssum = arr[j+1][i+1]
            tsum = sum(arr[j+2][i:i+3])
            hourglass = fsum + ssum + tsum
            # print(message.format(f=fsum, s=ssum, t=tsum, h=hourglass))
            sums.append(hourglass)
    sums.sort()
    return sums[-1]


file = open("./data", 'r')
a = []
for _ in range(6):
    a.append(list(map(int, file.readline().split())))
print(hourglassSum(a))

