n = int(input())
x = int(input())
y = int(input())
answer = 0


def check(number, x, y):
    global answer
    num_set = set(str(number))
    if len(num_set) == 1:
        if str(x) in num_set or str(y) in num_set:
            answer += 1
        return
    if len(num_set) == 2:
        if str(x) in num_set and str(y) in num_set:
            answer += 1


def do_task(n, x, y):
    for i in range(n + 1):
        check(i, x, y)

    if answer == 0:
        print(-1)
        return

    print(answer)


do_task(n, x, y)
