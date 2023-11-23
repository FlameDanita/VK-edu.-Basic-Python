def filter(func, seq):
    for elem in seq:
        if func(elem):
            yield elem
               

func_in, seq_in = eval(input()), eval(input())

for x in filter(func_in, seq_in):
   print(x)