stackl=[]
stackr=[]
left='([{'
right=')]}'
s=input('请输入判断语句：')
for i in s:
    if i==left:
        stackl.append(i)
        changdul=len(stackl)
    elif i==right:
        stackr.append(i)
        changdur=len(stackr)
        if changdul<changdur:
            print("不匹配")
            break
        else:
            continue
    else:
        continue
print(stackl.pop())
print(stackr.pop())
if chuzhanl == '( 'and chuzhanr==')'  or chuzhanl == '[' and chuzhanr == ']':
    print('匹配')
else:
    print('不匹配')
if chuzhanl == '{'and chuzhanr=='}':
    print('匹配')
else:
    print('不匹配')