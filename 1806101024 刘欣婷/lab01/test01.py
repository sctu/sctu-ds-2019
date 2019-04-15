#编程实现字符串反转
#输入：Hello,World!
#输出:!dlroW,olleH
#字符串里面的每一个字符进行压栈操作
#出栈直到栈为空为止，打印每个出栈元素

stack = []

for i in 'Hello,World!':
    stack.append(i)

result = []
while len(stack) != 0:
    result.append(stack.pop())
print("".join(result))
