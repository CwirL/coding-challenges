class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = None

    def computeDifference(self):
        differences = []
        for i in self.__elements:
            for j in self.__elements:
                differences.append(abs(i-j))
        differences.sort()
        self.maximumDifference = differences[-1]


_ = input()
a = [int(e) for e in input().split(' ')]
d = Difference(a)
d.computeDifference()
print(d.maximumDifference)
