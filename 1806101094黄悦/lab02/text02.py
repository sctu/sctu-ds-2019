# 编程实现括号匹配。
# 输入：{[()]}
# 输出：True
stack=[]
LEFT=['{','[','[']
RIGHT=['}',']','）']
#以次遍历每一个字符
for i in '{[()]}':
    #左括号怎么处理:如果是左括号,压栈
    if i in LEFT:
        #print(i)#运行测试
       stack.append(i)
     #右括号怎么处理：如果是右括号，
    if i in RIGHT:
       # print(i)#测试
       #定义变量左括号
       left_parentheses=stack.pop()
       #当前左括号下标
       left_index=LEFT.index(left_parentheses)
       #当前右括号下标
       right_index=RIGHT.index(i)

       if left_index!=right_index:
           print('不匹配')
           break#跳出整个for循环

#当所有字符处理完成后
if len(stack) is 0:
    print('匹配')
else:
    print('不匹配')
