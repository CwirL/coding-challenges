import sys

if __name__ == "__main__":
    n = int(input())
    tel = {}
    for i in range(n):
        data = input()
        name, number = data.split()
        tel[name]=number
    while True:
        try:
            query = input()
            if query in tel.keys():
                print(query + '=' + tel[query])
            else: 
                print('Not found')
        except EOFError:
            sys.exit()