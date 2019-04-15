print('hello,world')
stack = []
for i in 'hello,world':
    stack.append(i)

while len(stack) !=0:
    print(stack.pop())

result=[]
while len(stack) is not 0:
    result.append(stack.pop())