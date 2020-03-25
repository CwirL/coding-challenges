cal = open('./calculated', 'r')
ex = open('./exptected', 'r')

calarr = list(map(int, cal.readline().strip()))
exarr = list(map(int, ex.readline().strip()))
print(calarr == exarr)