a=input("请输入：")
b=['(','{','[']
c=[')','}',']']

stack=[]
for i in a:
    if i in b:
        stack.append(i)
    elif i in c:
        if len(stack)==0:
            stack.append(1)
            break
        elif b.index(stack[-1])==c.index(i):
            stack.pop()
        else:
            break

if len(stack) == 0:
    print('匹配')
else:
    print('不匹配')