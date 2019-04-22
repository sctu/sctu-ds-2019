#编程实现字符串反转
#输入：Hello,World!
#输出：!dlroW,olleH

# 字符串里面的每一个字符进行压栈
# 出栈 直到栈空为止 打印每个出栈元素

stack=[]
for i in "hello,world!":
    stack.append(i)
# print(stack.pop())#confirm if its right
result=[]
while len(stack) is not 0:
    result.append(stack.pop())

print("".join(result))
