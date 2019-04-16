

#输入：Hello World!
#输出：!dlroW,olleH

#1. 将每个字符压栈
stack=[]

for i in 'Hello,World!':
    stack.append(i)
#2. 出栈直到栈为空为止，并且打印每一个字符


'''
result=[]
while len(stack) is not 0:
    result.append(stack.pop())
print(''.join(result))
'''


while len(stack) != 0:
    a=stack.pop()
    print(a)

