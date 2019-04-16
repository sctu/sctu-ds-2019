#字符串倒转
stack=[]
str=input("请输入：")
for i in str:
    stack.append(i)
while len(stack) is not 0:
    print(stack.pop())