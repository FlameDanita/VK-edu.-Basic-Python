strings = input().split(" ")

sum_length = 0
count_strings = 0

for i in strings:
    if i != '':
        sum_length += len(i)
        count_strings += 1

res = sum_length / count_strings

print(round(res, 2))