stack=[]
s="hello world"
for i in s:
    stack.append(i)
while len(stack)!=0:
    print(stack.pop(),end="")

