num=input("请输入括号：")
stack=[]
for i in num:
    if i is "("or\
            i is "["or\
            i is "{":
        stack.append(i)
    #elif i==")"or"]"or"}":
    #stack.pop()


print(stack.pop())
print(stack.pop())
