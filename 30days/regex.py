import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    pattern = r"^[a-z0-9](\.?[a-z0-9]){1,}@g(oogle)?mail\.com$"
    names = []
    for i in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        if re.match(pattern, emailID):
            names.append(firstName)
    names.sort()
    for name in names:
        print(name)
