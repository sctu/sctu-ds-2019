str='abcdcba'
stack=[]
for i in str:
    stack.append(i)
q= []
while len(stack) is not 0:
    q.append((stack.pop()))

a=''.join(q)
if a==str:
    print(True)
else:
    print(False)
