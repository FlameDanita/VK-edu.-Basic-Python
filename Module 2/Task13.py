def cache_deco(func):
   cache = {}
   def wrapper(*args):
      if args in cache:
         return cache[args]
      else:
         result = func(*args)
         cache[args] = result
         return result
      
   return wrapper

def solution(func_map, func_filter, data):
   filtered_data = (x for x in data if func_filter(x))
   mapped_data = (func_map(x) for x in filtered_data)
   result = (x for i, x in enumerate(mapped_data) if i % 2 == 1)
   return result

# code = []
# while data := input():
#   code.append(data)
# code = "\n".join(code)
# exec(code)

def calc():
   count = 0
   @cache_deco
   def calc_(x):
      nonlocal count
      count += 1
      print("Call:", count)
      return x
   return calc_

for i in solution(calc(), lambda x: x % 2 == 1, (1, 1, 2, 2, 2, 3, 1, 2, 3, 1)):
   print(i)