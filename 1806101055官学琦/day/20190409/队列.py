n=input()
queue=[]
for i in n:
    queue.append(i)
while len(queue)!=0:
    print(queue.pop(0),end="")
