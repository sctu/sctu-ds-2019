s='hello world!'
def func(s):
    l = list(s)
    result = ""
    while len(l)>0:
        result += l.pop()
    return result
result = func(s)
print(func(s))