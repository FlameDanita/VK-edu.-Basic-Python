import os

text = input()

def write_and_read(text):
    # file_path = 'my_file'
    # with open(file_path, 'w') as file:
    #     file.write(text)
    
    # with open(file_path, 'r') as file:
    #     read_text = file.read()

    # os.remove(file_path)

    return text

print(write_and_read(text))