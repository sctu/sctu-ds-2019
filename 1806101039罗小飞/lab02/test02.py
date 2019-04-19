stackl=[]
# p=0
# o=0
left=['(','[','{']
right=[')',']','}']
a=input('请输入判断括号(注意：若输出多则结果，出现“不匹配”则视该结果为有效！):')
for i in a:
    if i=='(' or i=='[' or i=='{':
        stackl.append(i)
    elif i==')' or i==']' or i=='}':
        if len(stackl)== 0:
            print('不匹配')# p=p+1
        else:
            s = stackl.pop()
            z = left.index(s)
            x = right.index(i)
            if z==x:
                if len(stackl)!=0:
                    continue
                else:
                    print('匹配')# o=o+1
            else:
                print('不匹配')# p=p+1
    else:
        continue
if len(stackl)!=0:
    print('不匹配')
#     p=p+1
# if p!=0:
#     print('不匹配')
# elif o==0 and p==0:
#     print('您输入的不是正确的括号格式！')
# else:
#     print('匹配')