#编程实现字符串反转
#输入：hello,world!
#输出：!dlrow,olleh
# 字符串里面的每一个字符实施压栈操作
stack=[]
for i in "hello,world!":
    stack.append(i)
#测试每一步是否正确
while len(stack)!=0:
    print(stack.pop(i))
# 出栈，直到栈为空为止，打印每个出栈元素
result=[]
while len(stack) is not 0:
    result.append(stack.pop())
print(result)
