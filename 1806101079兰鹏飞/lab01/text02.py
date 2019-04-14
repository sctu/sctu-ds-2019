str=input()
match={'[':']','(':')','{':'}'}
stack=[]
status=0
for i in str:
    if i in match.keys():
        stack.append(i)
    elif i in match.values():
        if len(stack)!=0 :
            if match[stack[-1]]==i:
                stack.pop()
            else:
                status=1
                break

        else:
            status=1
            break
if status==0:
    print('匹配成功')
else:
    print('匹配失败')