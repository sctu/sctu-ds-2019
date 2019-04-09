# 1、编程实现字符串反转。
#
# 输入：Hello,World!
#
# 输出：!dlroW,olleH
str=input()
stack=[]
for i in str:
    stack.append(i)
while len(stack)!=0:
    print(stack.pop(),end="")