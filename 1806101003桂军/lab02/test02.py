def match_parentheses(s):
    # 把一个list当做栈使用
    ls = []
    parentheses = "()[]{}"
    for i in range(len(s)):
        si = s[i]
        # 如果不是括号则继续
        if parentheses.find(si) == -1:
            continue
        # 左括号入栈
        if si == '(' or si == '[' or si == '{':
            ls.append(si)
            continue
        if len(ls) == 0:
            return False
        # 出栈比较是否匹配
        p = ls.pop()
        if (p == '(' and si == ')') or (p == '[' and si == ']') or (p == '{' and si == '}'):
            continue
        else:
            return False
    if len(ls) > 0:
        return False
    return True
if __name__ == '__main__':
    s = "{abc}{de}(f)[(g)"
    result = match_parentheses(s)
    print(s, result)
    s = "0{abc}{de}(f)[(g)]9"
    result = match_parentheses(s)
    print(s, result)
