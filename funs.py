import re
def find_number(s):
    arr = re.findall(r"\d+\.?\d*",s)
    return arr
def say_hello():
    print('hello')
def say_something(s):
    print(s)
