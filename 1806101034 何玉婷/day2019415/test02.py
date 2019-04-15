#编程实现括号匹配

stack=[]
LEET=['{','[','(']
RIGHT=['}',']',')']

#依次遍历每一个字符
for i in '{[()]}':
    #如果当前字符是左括号，压栈
   if i in LEET:
       #print（i）
    stack.append(i)

    #如果当前字符是右括号，
     for i in RIGHT:
         #print(i)
         left_parentheses = stack.pop()

         left_index = LEET.index(left_parenthesess).
         right_index = RIGHT.index(i)

         if left_index ！right_index:
             print('不匹配')
             break


# 当所有字符处理完成后
if len(stack) is 0：
    print('匹配')
else:
    print('不匹配')
