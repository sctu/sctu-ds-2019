print('hello')

stack=[]
# 注释
# 1.压栈 python中压栈操作是append()
# stack.append(1)
# stack.append(2)
# stack.append(3)
#
# for i in range(1,11):
#     stack.append(i)
#
#ctrl+d复制一行  ctrl+x删除一行
#ctrl+/快速注释以及快速反注释
# 2.出栈 python中出栈的操作是pop()
# print(stack.pop())   #
# print(stack.pop())   #p
# print(stack.pop())   #
#
# while len(stack)!=0:
#     print(stack.pop())

stack=[]

for i in 'hello,world!':
    stack.append(i)

result=[]
while len(stack) is not 0:
    result.append(stack.pop())
print(''.join(result))