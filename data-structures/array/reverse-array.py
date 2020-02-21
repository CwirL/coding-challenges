def reverseArray(a):
    n = len(a)
    s = 0
    e = n-1
    while s < e:
        a[s], a[e] = a[e], a[s]
        s += 1
        e -= 1
    return a


print(reverseArray([2, 3, 4, 1]))