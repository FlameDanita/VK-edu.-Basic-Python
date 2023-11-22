def fun_3(start, end, step):
    seq = range(start, end, step)
    for i in map(lambda x: x**2 if x % 2 != 0 else -x, seq):
        print(i)


string = input().split()
fun_3(int(string[0]), int(string[1]), int(string[2]))

