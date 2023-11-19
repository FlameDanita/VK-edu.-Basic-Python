# string = "Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming.".lower().split(' ')

string = input().lower().split(' ')

d = {string.count(v): v for v in string}

print(d[max(d.keys())], max(d.keys()))
 