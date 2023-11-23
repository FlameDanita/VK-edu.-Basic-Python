def map(func, seq):
    for elem in seq:
        yield func(elem)

func_in, seq_in = eval(input()), eval(input())

for x in map(func_in, seq_in):
    print(x)