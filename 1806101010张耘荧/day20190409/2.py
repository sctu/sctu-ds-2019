num = input("请输入括号：")
stack = []
for i in num:
    if i is "("or\
            i is "["or\
            i is "{":
        left = stack.append(i)
    elif i == ")" or "]" or "}":
        right = stack.pop()
if left.index(i) == right.index(i):

    '''elif i == ")":
        s = stack.pop()
        if s == "(":
            continue
        else:
            print("不匹配")
    elif i == "]":
        s=stack.pop()
        if s == "[":
            continue
        else:
            print("不匹配")
    elif i == "}":
        s=stack.pop()
        if s == "{":
            continue
        else:
            print("不匹配")
if len(stack)%2!=0:
    print("不匹配")
else:
    print("匹配")

'''




