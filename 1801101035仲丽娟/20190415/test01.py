#1.编程实现字符串反转
#输入：Hello，World！
#输出：！dlroW，olleH
#字符串里的每一个字符进行压栈操作，出栈直到栈为空，打印每个出栈元素

stack = []
for i in'Hello,World!':
    stack.append(i)
    #测试第一步正确
# while len(stack) != 0:
   # print(stack.pop())
while len(stack) != 0:
    print(stack.pop())