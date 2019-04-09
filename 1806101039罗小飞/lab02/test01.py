stack=[]
# stack.append(1)
# stack.append(2)
# stack.append(3)
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
for i in range(1,10):
    stack.append(i)
while len(stack) !=0:
    print(stack.pop())