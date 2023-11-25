import datetime

days, seconds = int(input()), int(input())

def shift_time(days: int, seconds: int):
    shift = datetime.datetime(2023, 1, 1, 12, 30) + datetime.timedelta(days=days, seconds=seconds) 
    return (int(shift.strftime("%d")), int(shift.strftime("%S")))

print(shift_time(days, seconds))