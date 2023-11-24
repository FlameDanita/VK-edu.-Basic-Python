class Dictionary:
    def __init__(self, dictionary):
        self.d = dictionary

    def __call__(self, key):
        return self.d[key]

# code = []
# while data := input():
#    code.append(data)
# code = "\n".join(code)
# exec(code)

dictionary = Dictionary({1:2, 2:1, 3:3})
print(dictionary(1))
# print(dictionary.d)