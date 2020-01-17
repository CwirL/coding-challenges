class Calculator:
    def power(self, base, exponent):
        if base < 0 or exponent < 0:
            raise Exception('n and p should be non-negative.')
        return base**exponent


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)