#编程实现括号匹配
def match_parentheses(s):

    ls = []    # 把一个list当做栈使用
    parentheses = "()[]{}"
    for i in range(len(s)): # 遍历他的每一个字符
        si = s[i]

        if parentheses.find(si) == -1:  # 如果不是括号则继续
            continue

        if si == '(' or si == '[' or si == '{':  # 如果是左括号入栈
            ls.append(si)
            continue
        if len(ls) == 0:
            return False
        p = ls.pop()
        if (p == '(' and si == ')') or (p == '[' and si == ']') or (p == '{' and si == '}'):   # 如果是右括号则出栈比较是否匹配
            continue
        else:
            return False
    if len(ls) > 0:    # 判断栈是否为空
        return False
    return True
if __name__ == '__main__':
    s = "{}{}()[()"
    result = match_parentheses(s)
    print(s, result)
    s = "{}{}()[()]"
    result = match_parentheses(s)
    print(s, result)
