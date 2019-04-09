#定义匹配括号函数
def match_parentheses(s):
    #定义栈
    stack = []
    parentheses = "()[]{}"
    #判断是否为括号
    for i in range(len(s)):
        si = s[i]
        if parentheses.find(si) == -1:
            continue
        #是括号就压入
        if si == '(' or si == '[' or si == '{':
            stack.append(si)
            continue
        if len(stack) == 0:
            return False
        p = stack.pop()
        if (p == '(' and si == ')') or (p == '[' and si == ']') or (p == '{' and si == '}'):
            continue
        else:
            return False
    if len(stack) > 0:
        return False
    return True
if __name__ == '__main__':
    s = "{abc}{de}(f)[(g)"
    result = match_parentheses(s)
    print(s, result)
    s = "0{abc}{de}(f)[(g)]9"
    result = match_parentheses(s)
    print(s, result)