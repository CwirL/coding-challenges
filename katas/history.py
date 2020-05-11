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