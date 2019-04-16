#括号配对判断
stack=[]
stack0=input('请输入需要括号配对判断：')

stack1={'{':'}','[':']','(':')'}


left=stack1.keys()
right=stack1.values()
a=0

for ch in stack0:
    if ch in left:
        stack.append(ch)
    elif ch in right:
        if ch==stack1[stack[-1]]:
            stack.pop()
        else :
            a=1

if a==1:
    print(False)
else :
    print(True)