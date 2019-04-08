# print('hello')
# stack = []
# 注释
# 1. 压栈 python中压栈操作是append()
# stack.append(1)
# stack.append(2)
# stack.append(3)

# for i in range(1, 11):
#     stack.append(i)
# # Ctrl+D 复制一行
# Ctrl+X 删除一行
# Ctrl+/ 快速注释

# 2.出栈 python中出栈的操作是pop（）
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# while len(stack) != 0:
#     print(stack.pop())
# while len(stack) is not 0:
#     print(stack.pop())
#     str = 'Hello,World'
stack = []
for i in 'Hello,World':
    stack.append(i)
while len(stack) is not 0:
    print(stack.pop())
