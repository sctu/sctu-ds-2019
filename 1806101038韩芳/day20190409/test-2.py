shuru=input()
stack=[]
left=['(','[','{']
right=[')',']','}']
for i in shuru:
    if i in  left:
        stack.append(i)

    if i in right:
        print(right.index(i))
        if left[right.index(i)]==stack[-1]:
            stack.pop()
            print('成功')
        else:
            print('错误')

