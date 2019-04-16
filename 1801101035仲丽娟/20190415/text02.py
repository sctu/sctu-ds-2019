#2、编程实现括号匹配。
#输入：{[()]}
#输出：True
#依次遍历每一个字符，如果是左括号则压栈，如果是右括号出栈，
# 并且出栈的元素和当前的右括号进行匹配，匹配则继续，不匹配则返回FALSE
#返回TRUE，所有字符都处理完成
#返回false,当所有字符处理完成后，栈不为空

#定义一个集合
LEFT=['{','[','(']
RIGHT=['}',']',')']
#依次遍历每一个字符
for i in'{[()]}':
    #如果左括号，压栈
    if i in LEFT:
       #print(i)
    stack.append(i)
if i in RIGHT:
       #print(i)
     left_parentheses=stack.pop()
#当前左括号下标
       left_index=LEFT.index(left_parentheses)
#当前右括号下标
       left_index=right.idex(i)

       if left_index !=right_index:
           print('不匹配')
           break
#当所有字符处理完成后
if (stack)is 0
    print('匹配')
else:
    print('不匹配')