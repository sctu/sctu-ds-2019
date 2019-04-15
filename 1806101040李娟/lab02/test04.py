str = input("please input something:")
stack = []
for i in str:
    stack.append(i)
min=[]
min.append(stack.pop())
print(min)
while len(stack) != 0:
    if stack[-1]<min[-1]:
        min.append(stack.pop())