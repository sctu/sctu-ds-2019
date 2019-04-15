#编程实现字符串反转。
#输入：Hello,World!
#输出：！dlroW,olleH
#步骤：
#1.字符串里面的每一个字符进行压栈操作。
#2.出栈直到栈为空，打印每个出栈元素。

stack=[]#定义一个栈
for i in 'Hello,Word!':# i 每一个字符压栈操作
    stack.append(i)
#测试第一步完全正确
#while Len(stack)!=0:
#     print(stack.pop())
result=[]#列表
while len(stack)!=0:
   result.append(stack.pop())
print(''.join(result))


