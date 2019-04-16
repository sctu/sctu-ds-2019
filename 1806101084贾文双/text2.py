str='[{(}]'
stack=[]
left=['[','{','(']
right=[']','}',')']
for i in str:
    if i in left:
        stack.append(i)
    elif i in right:


        if i in right:

            if len(stack)==0:
                stack.append(0)
                break
            else:
                stack.pop()
        else:
            print("False")
            break

if len(stack)!=0:
    print("False")
else:
    print("True")
