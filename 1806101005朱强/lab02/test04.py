# 编程实现字符串反转。

输入：Hello,World!

输出：!dlroW,olleH

#字符串里的每一个字符进行压栈操作。
stack = []
for  i in 'hello,world!':
    stack.append(i)
    result = []
    while len(stack) != 0:
        result.append(stack.pop())
         print("".join(result)






#出栈直到栈为空为止，打印出每一个出栈元素。
while len(stack) is not 0:
    result.append(stack.pop())