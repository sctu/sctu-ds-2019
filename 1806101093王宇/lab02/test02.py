text = "{[()]}"
def is_closed(text:str):
    stack = []
    brackets = {')':'(',']':'[','}':'{'}
    for char in text:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if brackets[char] != stack.pop():
                return False
    return True

print(is_closed(text))



