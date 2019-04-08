# # print('hello')
#
# stack = []
#
# # 注释
# # 1. 压栈 python中压栈操作是append()
# # stack.append(1)
# # stack.append(2)
# # stack.append(3)
#
# for i in range(1, 11):
#     stack.append(i)
#
# # ctrl+d    复制一行
# # ctrl+x    删除一行
# # ctrl+/    快速注释
#
# # 2. 出栈 python中出栈的操作是pop()
# # print(stack.pop())  #
# # print(stack.pop())  #
# # print(stack.pop())  #
#
# while len(stack) is not 0:
#     print(stack.pop())


# 1、编程实现字符串反转。
#
# 输入：Hello,World!
#
# 输出：!dlroW,olleH

stack = []

for i in 'hello,World!':
    stack.append(i)

result = []
while len(stack) is not 0:
    result.append(stack.pop())
print(''.join(result))
