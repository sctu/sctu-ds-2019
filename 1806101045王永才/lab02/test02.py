SYMBOLS = {'}': '{', ']': '[', ')': '(', '>': '<'}
SYMBOLS_L, SYMBOLS_R = SYMBOLS.values(), SYMBOLS.keys()

def check(s):
    arr = []
    for c in s:
        if c in SYMBOLS_L:
            # 左符号入栈
            arr.append(c)
        elif c in SYMBOLS_R:
            # 右符号要么出栈，要么匹配失败
            if arr and arr[-1] == SYMBOLS[c]:
                arr.pop()
            else:
                return False

    return True
print(check("3 * {3 +[(2 -3) * (4+5)]}"))
print(check("3 * {3+ [4 - 6}]"))