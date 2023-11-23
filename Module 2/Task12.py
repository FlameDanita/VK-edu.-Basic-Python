from typing import List, Dict

def make_most_common_keys(d: Dict[int, int]) -> List[int]:
   
    lst = []
    for key in sorted(d.items(), key=lambda item: item[1], reverse=True):
        lst.append(key[0])
        
    return lst

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

# d = {5:3, 3:5, 0:2, 4:6, 7:10}
# print(make_most_common_keys(d))
