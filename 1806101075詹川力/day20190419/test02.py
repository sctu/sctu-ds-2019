#编程实现括号匹配。
#{[()]}
 stack = []
 LEFT = ["{" "[" "("]
 RIGHT = ["}" "]" ")"]

#1.遍历字符串的每一个字符
 for i in "{[()]}":
     print(i)
#2.如果当前字符是左括号，则入栈。
   if i in LEFT:
       stack.append(i)
#3.如果当前字符是右括号，
#  则出栈一个字符进行匹配。
   if i in RIGHT:
       left_parentheses = stack.pop()
       //判断左右括号是否匹配
       if LEFT.index(left_parentheses) \
               ！= RIGHT.index（i）：
           print("不匹配")
           break
#4.当所有的字符都处理完成后，
#  判断栈是否为空。
if len(stack) is 0：
    print("匹配")
else:
    print("不匹配")
