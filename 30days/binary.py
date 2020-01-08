import math
import os
import random
import re
import sys

if __name__ == "__main__":
    n = int(input())
    binaryRev = []
    previousbin = None
    oneSet = []
    i = 0
    first = True
    while True:
        if (n==0 or n==1):
            if (n == 1 and n == previousbin or first):
                i = i+1
            oneSet.append(i)
            binaryRev.append(n)
            break
        reminder = n//2
        quotient =  n%2
        binaryRev.append(quotient)
        n = reminder
        if (quotient == 1 and first):
            i = i + 1
            first = False
        if (quotient == 1 and quotient == previousbin):
            i = i+1
        if (i>1 and quotient == 0):
            oneSet.append(i)
            i = 1
        previousbin = quotient
    binary = []
    for j in reversed(binaryRev):
        binary.append(j)
    oneSet.sort()
    print(oneSet[-1])