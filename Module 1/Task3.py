a, b = int(input()), int(input())

flag = True

while n := input():
    if int(n) < a or int(n) > b:
        flag = False

print(flag)