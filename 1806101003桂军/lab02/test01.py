#编程实现字符串反转
#输入：Hello,Word!
#输出：！dlroW,olleH
#将每一个字符压栈
stack = []                            #将列表当作一个栈使用
for i in 'hello,World!':              #遍历每一个字符
    stack.append(i)                   #对每一个字符压栈
result = []                           #创建一个新的栈
while len(stack) != 0:                #栈不为空时就一直出栈
    result.append(stack.pop())        #出栈时并压入另一个栈
print("".join(result))                #打印出每一个字符