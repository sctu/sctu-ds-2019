# 2、编程实现括号匹配。
#
# 输入：{[()]}
#
# 输出：True


str=input()
match={'[':']','(':')','{':'}'}
stack=[]
flag=0
for i in str:
    if i in match.keys():
        stack.append(i)
    elif i in match.values():
        if len(stack)!=0 :
            if match[stack[-1]]==i:
                stack.pop()
            else:
                flag=1
                break

        else:
            flag=1
            break
if flag==0:
    print('匹配成功')
else:
    print('匹配失败')
