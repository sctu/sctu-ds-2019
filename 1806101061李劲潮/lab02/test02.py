def parCheker(str):
    s = Stack()
    balanced = True
    index = 0
    while index<len(str) and balanced:
        str1 = str[index]
        if str1 in '([{':
            s.push(str1)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,str1):
                    balanced = False

        index += 1

    if s.isEmpty() and balanced:
        return True
    else:
        return False


def matches(open,close):
    opens = '([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)