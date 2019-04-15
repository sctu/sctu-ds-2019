#   stack.pop()    将栈中当前元素出栈
stack=[]
for i in "Hello,Word!":
    stack.append(i)

#  处理栈，当栈为空的时候结束循环
while len(stack) != 0:
    print(stack.pop())


