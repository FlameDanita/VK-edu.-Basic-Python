def fub(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fub(n - 1) + fub(n - 2)
    
print(fub(int(input())))