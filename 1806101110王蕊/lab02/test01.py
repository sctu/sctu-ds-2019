
#  编程实现字符串反转。
#  输入：Hello,World!
#  输出：!dlorW,olleH
#  字符串里面的每一个字符进行压栈操作
#  出栈直到栈为空为止，打印每一个出栈元素


stack = []   #  定义一个栈
for i in "Hello,World!":
    stack.append(i)

#测试第一步完全正确
# while len(stack) !=0:
#   print(stack.pop())
result = []
while len(stack) is not 0:
    result.append(stack.pop())
print("",(result))
