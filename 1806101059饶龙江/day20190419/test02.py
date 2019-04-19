
S=[]#创建一个空列表作为栈
a=input()
for i in a:#遍历给定的括号字符串
    if i=='('or i=='{'or i=='[':
        S.append(i)#判断单个括号是否属于左括号，如果属于，将他压入栈；
        continue
    elif i==')'or i=='}'or i==']':
        if len(S)==0:
            S.append(i)
            break
            print(False)
            # 如果不属于，先判断栈是否为空，如果为空，将它压入栈后输出False，
        else:
            q = S.pop()
            # 若不为空则弹出一个栈中的元素
        if i==')'and q=='(':
            continue
        elif i=='}'and q=='{':
            continue
        elif i==']'and q=='[':
            continue
            #并判断出栈的括号和此时遍历的括号是否匹配，匹配则继续
        else:
            print(False)
            # 若不匹配，则停止遍历输出False，

if len(S)==0:
    print(True)
    # 如果所有的元素遍历完，且最后栈中无剩余元素、则输出Ture；
else:
    print(False)
    # 如果所有的元素遍历完，且最后栈中有剩余元素，输出False
