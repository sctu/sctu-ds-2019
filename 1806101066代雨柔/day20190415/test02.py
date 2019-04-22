#2、编程实现括号的匹配
stack=[]
left=["{","[","("]
right=["}","]",")"]
#一次遍历每一个字符
for i in "{[()]}":
    #左括号怎么处理:压栈
    if i in left:
        #print(i)
        stack.append(i)
    #如果当前是右括号怎么处理：
    if i in right:
       # print(i)
       LEFT_parentheses=stack.pop()
             #(括号)
       LEFT_index=left.index(LEFT_parentheses)
           #（下标）
       RIGHT_index=right.index(i)
       if LEFT_index!=RIGHT_index:
            print('不匹配')

if len(stack) is 0:
    print('匹配')
else:
    print('不匹配')
    #当所有字符都处理完成后
#输入:{[()]}
#输出：True

#3、编程实现回文数判断
#1）一分为二
#   左边所有字符入栈，右边所有字符入队列
#2）栈和队列依次各出一个元素
#   左边元素！=右边元素    不是回文
#3）当栈为空队列为空就是回文


#输入'abcdcba'
#输出'True'
str=input()
match={'[':']','(':')','{':'}'}
stack=[]
status=0#记录错误
for i in str:
    if i in match.keys():#如果是左括号就压栈
        stack.append(i)
    elif i in match.values():#如果是右括号
        if len(stack)!=0 :
            if match[stack[-1]]==i:#与栈顶括号匹配
                stack.pop()
            else:
                status=1
                break

        else:
            status=1
            break
if status==0:
    print('匹配成功')
else:
    print('匹配失败')
