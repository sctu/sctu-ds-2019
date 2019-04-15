# 1、编程实现字符串反转。
#
# 输入：Hello,World!
#
# 输出：!dlroW,olleH

stack = []
for i in "Hello,World!":
    stack.append(i)

while len(stack) is not 0:
    print(stack.pop(),end=" ")