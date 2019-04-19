stack=[]
left=["{","[","("]
right=[")","]","}"]
for i in "{[()]}":    #对字符串遍历
    if i in left:
        stack.append(i)
    if i in right:
        left_parentheses=stack.pop()
        A=left.index(left_parentheses)
        B=right.index(i)
    if A!=B:
        print("不匹配")
        break
if len(stack) is 0:
    print("匹配")
else:
    print("不匹配")
