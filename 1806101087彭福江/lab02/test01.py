#编程实现括号匹配。
#依次遍历每个字符
#左括号怎么处理
#右括号怎么处理

stack = []
left = ["{","[","("]
right = [")","]","}"]

for i in "{[()]}":
    if i in left:
        stack.append(i)

        
    if i in right:
        stack.pop()

