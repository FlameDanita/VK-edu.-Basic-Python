def string_trans(string):
    if string[0] == '!':
        string = string.upper()
    else:
        string = string.lower()

    string = string.replace('!', '').replace('@', '').replace('#', '').replace('%', '')

    return string

while True:
    string = input()
    if string:
        print(string_trans(string))
    else:
        break