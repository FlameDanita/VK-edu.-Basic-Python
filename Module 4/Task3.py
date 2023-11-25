from collections import defaultdict
from typing import List, Tuple


def fill_specializations(specializations: List[Tuple[str, str]]):
    dct = defaultdict(list)
    for el in specializations:
        if el[0] not in dct.keys():
            dct[el[0]] = [el[1]]
        else:
            dct[el[0]].append(el[1])
    return dict(dct)

# code = []
# while data := input():
#     code.append(data)
# code = "\n".join(code)
# exec(code)

specs=[('Sales', 'John Doe'), ('Sales', 'Martin Smith'), ('Accounting', 'Jane Doe'), ('Marketing', 'Elizabeth Smith'), ('Marketing', 'Adam Doe')]
print(fill_specializations(specs))