import datetime
from collections import Counter
from typing import List

def most_common_months(dates: List[str], n) -> List[int]:
    res = []
    for date in dates:
        elem = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
        res.append(int(datetime.datetime.strftime(elem, "%m")))

    result = []
    res = Counter(res).most_common(n)
    for rs in res:
        result.append(rs[0])
    
    return result



code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

dates=["2023-01-01T23:59:59", "2023-01-01T23:59:59", "2023-02-01T23:59:59"]
print(most_common_months(dates, 2))