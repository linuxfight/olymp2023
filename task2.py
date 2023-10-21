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

    colors_sum = sum(colors)

    colors_sum = colors_sum - colors[0] + 1

    print(colors_sum)

task(k)
