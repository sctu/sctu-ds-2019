#倒序输出hello word
stack = []

for i in "Hello,World":
    stack.append(i)#压栈

while len(stack) is not 0:#可以用来代替is not !=0
    print(stack.pop(),end="")
#   a = stack.pop()#出栈
#   print(a)


#print(stack.pop())
#while len(stack) is not 0:
#    print(stack.pop())