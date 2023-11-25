import datetime

string_datetime = input()

def parse_time(s):
    date = datetime.datetime.strptime(s, "%Y %m %d %H %M %S") + datetime.timedelta(days=1)
    return int(datetime.datetime.strftime(date, "%d"))

print(parse_time(string_datetime))