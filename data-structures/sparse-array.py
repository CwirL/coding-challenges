import re


def matchingStrings(strings, queries):
    sols = []
    for query in queries:
        rep = 0
        for word in strings:
            if word == query:
                rep += 1
        sols.append(rep)
    return sols


file = open('input', 'r')
strings_count = int(file.readline())
strings = []
for _ in range(strings_count):
    strings.append(file.readline().rstrip())

queries_count = int(file.readline())
queries = []
for _ in range(queries_count):
    queries.append(file.readline().rstrip())
print(strings)
print(queries)

res = matchingStrings(strings, queries)
for sol in res:
    print(sol)
