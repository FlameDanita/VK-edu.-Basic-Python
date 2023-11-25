from itertools import zip_longest
from typing import List, Tuple


def fill_missing_values(values_list_1: List[int], values_list_2: List[int]) -> List[Tuple[int, int]]:
    res = []
    for l1, l2 in zip_longest(values_list_1, values_list_2):
        if not l1:
            l1 = 1
        elif not l2:
            l2 = 1
        else:
            pass
        res.append((l1, l2))
    return res


code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

print(fill_missing_values([1, 2, 3], [2, 3, 4, 5]))

