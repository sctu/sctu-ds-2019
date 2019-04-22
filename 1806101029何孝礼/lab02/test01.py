stack=[]
for i in "hello,world!":
     stack.append(i)
list=[]
while len(stack)!=0:
     list.append(stack.pop())
print("".join(list))