stack=[]

stack.append(1)
stack.append(2)
stack.append(3)

for i in range(1,11):
    stack.append(i)



print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

while len(stack) is not 0:
    print(stack.pop())
