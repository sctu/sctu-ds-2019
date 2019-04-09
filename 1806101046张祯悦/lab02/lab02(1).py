# 第一题 编程实现字符串反转。
# 目标：
# input：Hello,World! output：!dlroW,olleH
stack = []#用“栈”来实现
for i in 'Hello,World!':#定义i为要反转的字符串
    stack.append(i)#append是附加，常用在for in的循环中
result = []#结果
while len(stack) is not 0:#返回对象
    result.append(stack.pop())#出栈
print(''.join(result))
