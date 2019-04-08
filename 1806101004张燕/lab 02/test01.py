

stack=[]
#注释
#1、压栈 push python中压栈的操作是append()

# stack.append(1)
# stack.append(2)
# stack.append(3)
# for i in range(1,11):
#     stack.append(i)
#ctrl+d复制 ctrl+x删除 ctrl+/快速注释以及反注释
#2、python中出栈的操作是pop()
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# while len(stack)!=0:
#     print(stack.pop())

stack=[]
for i in 'hello,world':
    stack.append(i)

result=[]
while len(stack) is not 0:
    result.append(stack.pop())
print(''.join(result))












