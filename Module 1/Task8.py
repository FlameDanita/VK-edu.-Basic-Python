n = int(input())

lists = []

for _ in range(n):
    buf = input().split()
    max_value = 0
    for i in range(len(buf)):
        if int(buf[i]) > max_value:
            max_value = int(buf[i])

    lists.append(max_value)

lists = sorted(lists)

for i in range(len(lists)):
    print(lists[len(lists) - i - 1], end='')
    if i != len(lists) - 1:
        print(';', end='')
