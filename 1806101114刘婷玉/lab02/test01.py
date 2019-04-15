# 1、编程实现字符串反转。
# 输入：Hello,World!
# 输出：!dlroW,olleH

stack = []

for i in 'hello,World!':  #利用栈先进后出
    stack.append(i)

result = []
while len(stack) is not 0:
    result.append(stack.pop())
print(''.join(result))
