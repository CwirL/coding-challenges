
actual = list(map(int, input().rstrip().split()))
expected = list(map(int, input().rstrip().split()))
yearDiff = actual[2] - expected[2]
monthDiff = actual[1] - expected[1]
dayDiff = actual[0] - expected[0]


def calculate_fee(days, months, years):
    if years > 0:
        fee = 10000
        return fee
    elif years < 0:
        return 0
    else:
        if months > 0:
            fee = 500 * months
            return fee
        if months < 0:
            return 0
        else:
            if days > 0:
                fee = 15 * days
                return fee
            else:
                return 0


print(calculate_fee(dayDiff, monthDiff, yearDiff))
