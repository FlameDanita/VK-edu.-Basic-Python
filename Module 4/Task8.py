from collections import deque
from typing import List

def rotate_list(nums: List[int], n: int):
   deq = deque(nums)

   for _ in range(n):
      num = deq.pop()
      deq.appendleft(num)

   return list(deq)

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

print(rotate_list([1,2,3,4], 2))