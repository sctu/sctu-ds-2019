#字符串反转

stack=[]

for i in 'hello,world!':
    stack. append(i)

result=[]
while len(stack) is not 0:
    result. append(stack. pop())
print(''.join(result))