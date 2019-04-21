
str=input()
stack=[]
num0=10

for i in str:
    stack.append(i)

while len(stack) is not 0:
    num1=int(stack.pop(0))
    if num1<num0:
        num0=num1
    else:
        num0=num0
print(num0)



