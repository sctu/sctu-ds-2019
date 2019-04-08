# print("hello world")
#
# stack=[]
#
# # 注释
# # 1. 压栈 python中压栈操作是append()
#
# for i in range(1,11):
#     stack.append(i)
# #ctrl+d(cpoy)  ctrl+x(delete) ctrl+/(defiing)
#
# #python中出栈的操作是pop()
# # print(stack.pop(9))
# while len(stack) is not 0:
#     print(stack.pop())
stack=[]
str1="Hello,world"
for i in "Hello,world!":
    stack.append(i)
result = []
while len(stack) is not 0:
    result.append(stack.pop())
print("".join(result))


