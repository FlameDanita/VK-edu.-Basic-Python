string = input()
count = 0

for i in string:
    if (i == '!' or i == '%' or i == '#' or i == '@'):
        count += 1

print(count)
print(string.lower().replace("!", '').replace("%", '').replace("#", '').replace("@", ''))