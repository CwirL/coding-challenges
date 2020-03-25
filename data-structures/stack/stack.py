n = int(input())
stack, maxStack = [], []
for _ in range(n):
    x, *b = map(int, input().split())
    if x == 1:
        stack.append(b)
        if not maxStack:
            maxStack.append(b)
        else:
            if b < maxStack[-1]:
                maxStack.append(maxStack[-1])
            else:
                maxStack.append(b)
    elif x == 2:
        stack.pop()
        maxStack.pop()
    else:
        print(*maxStack[-1])
