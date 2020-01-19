from functools import reduce
from math import ceil
from operator import itemgetter
'''
file = open("./input", 'r')
sampleSize = int(file.readline().strip())
samples = list(map(int, file.readline().split()))
'''
sampleSize = int(input().strip())
samples = list(map(int, input().split()))
# Mean
mean = round(reduce(lambda x, y: x+y, samples)/sampleSize, 1)
print(mean)
# Median
samples.sort()
if len(samples) % 2 == 0:
    i = len(samples)//2
    median = round((samples[i-1] + samples[i])/2, 1)
else:
    i = ceil(len(samples)/2)
    median = samples[i]
print(median)
# Mode
seen = {}
# Arrange duplicates in dict
for sample in samples:
    seen[sample] = 1 if sample not in seen else seen[sample] + 1
# Using itemgetter() to retrieve specific fields
mode = max(seen.items(), key=itemgetter(1))[0]
print(mode)
