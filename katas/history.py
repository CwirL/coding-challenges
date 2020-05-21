# kata # 1 - Multiply
def multiply(a, b):
    return a * b


# Kata # 2
sentence = "Hey fellow warriors"
sentenceArray = sentence.split()
reversed_sentence = ""
for sent in sentenceArray:
    if len(sent) > 4:
        reversed_sent = ""
        for char in reversed(sent):
            reversed_sent += char
    else:
        reversed_sent = sent
    if sent == sentenceArray[-1]:
        reversed_sentence += reversed_sent
    else:
        reversed_sentence += reversed_sent + " "
print(reversed_sentence)


# Kata # 3 - Find the odd int
def find_it(seq):
    unique_ints = set(seq)
    frequencies = {}
    for j in seq:
        for z in unique_ints:
            if z == j:
                if frequencies.get(z) is None:
                    frequencies[z] = 1
                else:
                    frequencies[z] += 1
                break
    for freq in frequencies:
        if frequencies[freq] % 2 != 0:
            return freq


# Kata # 4 - Array.diff
def array_diff(a, b):
    if len(a) == 0 or len(b) == 0:
        return a
    for number in b:
        a = list(filter(lambda x: x != number, a))
    return a


# kata # 5 - Create Phone Number
def create_phone_number(n):
    phone_number = '('
    for (idx, i) in enumerate(n):
        if idx == 3:
            phone_number += ') '
        elif idx == 6:
            phone_number += '-'
        phone_number += str(i)
    return phone_number


# kata # 6 - Highest and Lowest
def high_and_low(numbers):
    numbers = list(map(int, numbers.split()))
    return "{} {}".format(max(numbers), min(numbers))


# kata # 7 - RGB To Hex Conversion
def rgb(r, g, b):
    def int_to_hex(n):
        if n <= 0:
            return '00'
        if 1 <= n < 16:
            return '0' + hex(n)[-1].upper()
        elif n >= 255:
            return 'FF'
        else:
            return hex(n)[2:4].upper()
    return "{}{}{}".format(int_to_hex(r), int_to_hex(g), int_to_hex(b))


# kata # 8 - Take a Ten Minute Walk
def is_valid_walk(walk):
    if walk.length != 10:
        return False
    vertical = horizontal = 0
    for points in walk:
        if points == 'n':
            vertical += 1
            continue
        elif points == 's':
            vertical -= 1
            continue
        if points == 'e':
            horizontal += 1
            continue
        if points == 'w':
            horizontal -= 1
            continue
    if horizontal == 0 and vertical == 0:
        return True
    else:
        return False


# kata # 9 - Dubstep
def song_decoder(song):
    return " ".join(list(filter(lambda x: (x != ''), song.split("WUB"))))


# kata # 10 - Which are in?
def in_array(array1, array2):
    return sorted(list(set(a for a in array1 if " ".join(array2).find(a) != -1)))


# kata # 11 - Simple Pig Latin
def pig_it(text):
    return " ".join([a[1:] + a[0] + 'ay' if a.isalpha() else a for a in text.split()])


# kata # 12 - Human readable duration format
def format_duration(seconds):
    if seconds == 0: return "now"
    time_breaks = [31536000, 86400, 3600, 60]
    time_strs = ["year", "day", "hour", "minute"]
    date = []
    for time, time_srt in zip(time_breaks, time_strs):
        val = seconds // time
        if val > 0:
            val = seconds // time
            val = seconds // time
            date.append("{} {}".format(val, time_srt) if val == 1 else "{} {}s".format(val, time_srt))
            seconds %= time
    if seconds > 0:
        date.append("1 second" if seconds == 1 else str(seconds) + " seconds")
    return {1: "{}", 2: "{} and {}", 3: "{}, {} and {}", 4: "{}, {}, {} and {}", 5: "{}, {}, {}, {} and {}"}[len(date)].format(*date)


# kata # 13 - Maximum subarray sum
def max_sequence(arr):
    n = len(arr)
    diff = 1
    max_int = 0
    for i in range(len(arr)):
        for j in range(n):
            if sum(arr[j:j + diff]) > max_int:
                max_int = sum(arr[j:j + diff])
        diff += 1
        n -= 1
    return max_int


# kata # 14 - Pete, the baker
def cakes(recipe, available):
    return min([available[ingredient] // size] if ingredient in available else [0] for ingredient, size in recipe.items())[0]


# kata # 15 - The observed PIN
from itertools import product
def get_pins(observed):
    variations = {
        1: [1, 2, 4],
        2: [2, 1, 3, 5],
        3: [3, 2, 6],
        4: [4, 1, 5, 7],
        5: [5, 2, 4, 6, 8],
        6: [6, 3, 5, 9],
        7: [7, 4, 8],
        8: [8, 7, 5, 9],
        9: [9, 8, 6],
        0: [0, 8]
    }
    return [''.join(map(str, combination)) for combination in product(*[variations[int(digit)] for digit in observed])]


# kata # 16 - Prime factors
def is_prime(n):
    return not any(n % x == 0 for x in range(2, n))
class Primes:
    def __init__(self, n):
        self.primes_arr = [x for x in range(2, n) if n % x == 0]
        self.index = 0
    def get_prime(self):
        return self.primes_arr[self.index]
    def next_prime(self):
        self.index += 1
def factorize(n):
    primes = Primes(n)
    prime_factors = []
    while n > 1:
        if n % primes.get_prime() == 0:
            n /= primes.get_prime()
            prime_factors.append(primes.get_prime())
        else:
            primes.next_prime()
    return prime_factors
def sum_for_list(lst):
    prime_factors_map = {}
    lst += [sum(lst)]
    print(lst)
    for i in lst:
        prime_factors_map[i] = set(factorize(i))
    return prime_factors_map


# kata # 17 Calculator
from operator import add, sub, mul, truediv

class Calculator(object):
    def toFloat(self, el):
        try:
            print(el)
            return float(el)
        except:
            return el
    def evaluate(self, string):
        ops = {"/": truediv, "*": mul, "-": sub, "+": add}
        string = list(map(self.toFloat, string.split()))
        operands = list(map(float, [val for val in string if type(val) == float]))
        ops_str = [val for val in string if not type(val) == float]
        for op in ops:
            while op in ops_str:
                idx = ops_str.index(op)
                ops_str.pop(idx)
                new_value = ops[op](operands[idx], operands[idx + 1])
                operands = operands[:idx] + operands[idx + 2:]
                operands.insert(idx, new_value)
        return operands[0]