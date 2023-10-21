n = int(input())
a = int(input())
b = int(input())
c = int(input())

def task(n, a, b, c):
    if a > b or a > c:
        print(-1)
        return

    d = n - (b + c - a)

    print(d)


task(n, a, b, c)
