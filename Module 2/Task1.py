def get_arr_mean(arr):
    numbers = arr.split()
    numbers = list(map(int, numbers))

    return sum(numbers)/len(numbers)
    

while True:
    arr = input()
    if arr:
        print(get_arr_mean(arr))
    else:
        break
    