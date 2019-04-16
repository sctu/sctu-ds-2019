shuru=input()
stack=[]
for i in shuru:
    stack.append(i)
for i in shuru:

    if stack.pop()==i:
        print('成功')
    else:
        print('失败')
