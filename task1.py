n = int(input())
m = int(input())
a = int(input())
b = int(input())

def calculate_time(time, num):
    if time % num == 0:
        return 0
    return num - time % num

def task(n, m, a, b):
    time = n*60 + m

    if time == 480:
        print(0)
        return
    if time > 1320 or a == 841 or b == 841:
        print(-1)
        return
    if time < 480:
        base_time = 8 * 60
        a_time = calculate_time(base_time, a) + base_time - time
        b_time = calculate_time(base_time, b) + base_time - time
        if (a_time < b_time):
            print(a_time)
        elif a_time == b_time:
            print(a_time)
        else:
            print(b_time)
        return

    a_time = calculate_time(time, a)
    b_time = calculate_time(time, b)

    if (a_time < b_time):
        print(a_time)
    elif a_time == b_time:
        print(a_time)
    else:
        print(b_time)

task(n, m, a, b)