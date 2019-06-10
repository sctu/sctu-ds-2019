str = "{[()]}"
stack=[]
Left = "{[("
Right = "})]"

for i in str:
#左括号，入栈
    if i in Left:
        stack.append(i)

#右括号，匹配
    if i in Right:
        left = stack.pop()
        if len(stack) == 0:
            print("wrong")
            break
        print(left)
        print(i)
        if Left.index(left) != Right.index(i):
            print("匹配")
            break

if len(stack) == 0:
    print('ture')
else:
    print('wrong')


