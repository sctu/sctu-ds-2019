str=input()
match={'[':']','(':')','{':'}'}
stack=[]
status=0#记录错误
for i in str:
    if i in match.keys():#如果是左括号就压栈
        stack.append(i)
    elif i in match.values():#如果是右括号
        if len(stack)!=0 :
            if match[stack[-1]]==i:#与栈顶括号匹配
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