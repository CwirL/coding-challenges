t = int(input())
words = []
for i in range(t):
    word = input()
    words.append(word)

odd = ''
even = ''
for w in words:
    for letter, i in zip(w, range(len(w))):
        if (i == 0 or i%2 == 0):
            even += letter
        else:
            odd += letter
    print(even + " " + odd)
    odd = ''
    even = ''