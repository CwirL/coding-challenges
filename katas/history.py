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