import math
import os
import random
import re
import sys

if __name__ == '__main__':
    T = int(input())
    Sol = []
    for i in range(T):
        n, k = map(int, input().split())
        Sol.append(k - 1 if ((k - 1) | k) <= n else k - 2)
    for maxi in Sol:
        print(maxi)
