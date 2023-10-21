k = int(input())
colors = []

def sum(colors):
    sum = 0
    for color in colors:
        sum += color
    return sum

def task(k):
    for x in range(k):
        colors.append(int(input()))

    colors_length = len(colors)
    colors_sum = sum(colors)

    while colors_length > 1:
        colors_sum -= colors[colors_length - 1]
        colors_length -= 1

    colors_sum = sum(colors) - colors_sum + 1

    print(colors_sum)

task(k)
