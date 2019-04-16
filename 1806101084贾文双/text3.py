str=input()
stack=[]
queue=[]
result=[]
if len(str)%2==0:
    str1=str[0:len(str)//2]
    str2=str[-(len(str)//2):]
    for j in str2:
        queue.append(j)
    for i in str1:
        stack.append(i)
    while len(stack) is not 0:
        result.append(stack.pop())


elif  len(str)%2!=0:
    str1 = str[0:(len(str) // 2)+1]
    str2 = str[-((len(str) // 2)+1):]
    for j in str2:
        queue.append(j)
    for i in str1:
        stack.append(i)
    while len(stack) is not 0:
        result.append(stack.pop())
if queue==result:
    print("yes")
else:
    print("no")
