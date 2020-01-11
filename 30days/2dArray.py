import math
import os
import random
import re
import sys


def compare(pattern, hourglass):
    for i in range (7):
        if (pattern[i] != hourglass[i]):
            return False
    return True
    # notMatch = [(x,y) for i in range(6) if pattern[i] != hourglass]

def compareAllPatterns(hg):
    p1 = [1, 1, 1, 1, 1, 1, 1]
    p2 = [1, 1, 0, 0, 1, 1, 0]
    p3 = [1, 0, 0, 0, 1, 0, 0]
    p4 = [0, 0, 0, 0, 0, 0, 0]
    p5 = [0, 1, 0, 1, 0, 0, 2]
    p6 = [1, 0, 0, 1, 0, 2, 4]
    p7 = [0, 0, 0, 0, 2, 4, 4]
    p8 = [0, 0, 0, 0, 4, 4, 0]
    p9 = [1, 1, 1, 0, 0, 0, 0]
    p10 = [1, 1, 0, 2, 0, 0, 2]
    p11 = [1, 0, 0, 4, 0, 2, 0]
    p12 = [1, 0, 0, 4, 0, 2, 0]
    p13 = [0, 0, 2, 0, 0, 0, 1]
    p14 = [0, 2, 4, 0, 0, 1, 2]
    p15 = [2, 4, 4, 2, 1, 2, 4]
    p16 = [4, 4, 0, 0, 2, 4, 0]
    patterns = [p1, p2, p3, p4, p5, p6, p7, p8, p8, p10, p11, p12, p13, p14, p15, p16]
    for p in patterns:
        if(compare(p, hg)):
            return True

if __name__ == "__main__":
    """
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    """
    file = open('./data.txt', 'r')
    a = file.read()
    rows = a.rstrip().split('\n')
    arr = []
    for row in rows:
        arr.append(list(map(int, row.split(" "))))
    
    sums = []
    for i in range(6):
        for j in range(6):
            if (i<4 and j<4):
                hg = [arr[i][j], arr[i][j+1], arr[i][j+2], arr[i+1][j+1], arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2]]
                sum = 0
                for val in hg:
                    sum += val
                sums.append(sum)
    sums.sort()
    print(sums)
    print(sums[-1])