# 编程实现字符串反转

# 输入：Hello,world!

# 输出：!dlrow,olleH

# 1.字符串里面的每一个字符进行压栈操作。
stack = []
for i in 'Hello, world!':
    stack.append(i)

# 测试第一步完全正确
while len(stack) != 0:
    print(stack.pop())


# 出栈直到栈为空为止，打印每个出栈元素。
result = []
while len(stack) is not 0:
    result.append(stack.pop())
