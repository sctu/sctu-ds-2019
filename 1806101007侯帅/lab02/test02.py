#2、编程实现括号匹配。

#输入：{[()]}

#输出：True


S= {'}': '{', ']': '[', ')': '('}
#创建一个字典
SL, SR = S.values(), S.keys()
#键为右括号，键值为左括号

def sum(s):
    stack = []
    for ch in s:
    #针对每一个字符进行处理
        if ch in SL:
            # 左括号入栈
            stack.append(ch)
        elif ch in SR:
            # 右括号出栈，进行匹配，成功或者失败
            if stack and stack[-1] == S[ch]:
                stack.pop()
            else:
                return False
# 当所有字符都处理完后，栈不为空，返回False  如果栈为空，reture True
    return True
print(sum("3 * {3 +[(2 -3) * (4+5)]}"))
print(sum("3 * {3+ [4 - 6}]"))

#s.index('x')  获取x的下标