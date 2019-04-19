stack=[]
left=["{","[","("]
right=[")","]","}"]
for i in "{[()]}":    #对字符串遍历
    if i in left:
        stack.append(i)
    if i in right:
        left_parentheses=stack.pop()
        a=left.index(left_parentheses)
        b=right.index(i)
    if a!=b:
        print("不匹配")
        break
if len(stack) is 0:
    print("匹配")
else:
    print("不匹配")
