stackl=[]
stackr=[]
stackr2=[]
left=['(','[','{']
right=[')',']','}']
a=input('请输入判断括号 (若输出多个结果视第一个输出结果为有效！):')
if a[0] in right:
    print("不匹配")
else:
    for i in a:
        if i=='(' or i=='[' or i=='{':
            stackl.append(i)
        elif i==')' or i==']' or i=='}':
            stackr.append(i)
            while len(stackl)<len(stackr):
                print('不匹配')
        else:
            continue
    if len(stackl)==len(stackr):
        stackr2.append(stackr.pop())
        chuzhanl=stackl.pop()
        chuzhanr2=stackr2.pop()
        for q in chuzhanl:
                z=left.index(q)
        for w in chuzhanr2:
                x=right.index(w)
        print("不匹配") if z==x else print("匹配")
    else:
        print('不匹配')
